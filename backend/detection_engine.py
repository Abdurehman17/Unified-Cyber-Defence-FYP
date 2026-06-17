from collections import defaultdict
import time
import ai_engine 

# Traffic Stats
ip_traffic_stats = defaultdict(lambda: {'count': 0, 'start_time': time.time()})
port_scan_tracker = defaultdict(lambda: {'ports': set(), 'start_time': time.time()})

# === CONFIG ===
BLACKLISTED_IPS = ["8.8.8.8", "1.1.1.1"]
SAFE_IPS = ["192.168.18.1"] 
THREAT_SIGNATURES = ["cmd.exe", "root", "SELECT *", "DROP TABLE", "script>", "virus_test"]

def check_threats(packet_data):
    src_ip = packet_data['src']
    clean_ip = src_ip.split(' ')[-1] if ' ' in src_ip else src_ip
    
    if clean_ip in SAFE_IPS:
        return None 

    payload = packet_data.get('payload', "")
    packet_size = packet_data.get('size', 0) 
    dst_port = packet_data.get('dst_port', 0) 
    current_time = time.time()

    # 1. BLACKLIST CHECK
    if clean_ip in BLACKLISTED_IPS:
        return f"Blacklisted IP Detected: {clean_ip}"

    # 2. PAYLOAD CHECK
    if payload:
        for signature in THREAT_SIGNATURES:
            if signature in payload:
                return f"Malicious Payload Detected: '{signature}'"

    # 3. PORT SCAN CHECK
    p_stats = port_scan_tracker[clean_ip]
    if current_time - p_stats['start_time'] > 2.0:
        p_stats['ports'].clear()
        p_stats['start_time'] = current_time
        
    if dst_port > 0:
        p_stats['ports'].add(dst_port)
        
    if len(p_stats['ports']) > 15:
        p_stats['ports'].clear() 
        return f"Port Scanning Detected from {clean_ip}"

    # 4. DDOS CHECK 
    stats = ip_traffic_stats[clean_ip]
    if current_time - stats['start_time'] > 1.0:
        stats['count'] = 0
        stats['start_time'] = current_time
    stats['count'] += 1
    
    # Threshold for real Wi-Fi traffic
    if stats['count'] > 100:
        stats['count'] = 0 
        stats['start_time'] = current_time 
        return f"High Traffic (DDoS Flood) from {clean_ip}"

    # 5. AI BEHAVIORAL ANOMALY 
    # Shadowing Bypass: The AI checks the first 80 packets. If the connection 
    # exceeds 80 packets, it stays quiet so the DDoS engine can catch the massive flood.
    if stats['count'] <= 80:
        ai_prediction = ai_engine.detector.evaluate(packet_size, stats['count'])
        if ai_prediction == -1:
            return f"AI Behavioral Anomaly Detected from {clean_ip}"

    return None