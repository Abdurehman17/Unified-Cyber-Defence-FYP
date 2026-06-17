import socket
import time

# !!! CHANGE THIS TO LAPTOP 1's IP ADDRESS !!!
TARGET_IP = "192.168.18.17" 
PORT = 80

def print_header(title):
    print(f"\n{'='*40}\n>>> INITIATING: {title}\n{'='*40}")

def simulate_sqli():
    print_header("SQL Injection Attack")
    payload = b"DROP TABLE"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(payload, (TARGET_IP, PORT))
    print("Attack sent successfully!")

def simulate_xss():
    print_header("Cross-Site Scripting (XSS) Attack")
    payload = b"script>" 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(payload, (TARGET_IP, PORT))
    print("Attack sent successfully!")

def simulate_ddos():
    print_header("Volumetric DDoS Flood")
    print("Flooding over Wi-Fi...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_data = b"X" * 512
    
    # Blast packets. Real Wi-Fi will pace them perfectly.
    for _ in range(400):
        sock.sendto(packet_data, (TARGET_IP, PORT))
        time.sleep(0.001) 
    print("Flood complete. Packets sent.")

def simulate_ai_anomaly():
    print_header("Zero-Day Behavioral Anomaly (AI Test)")
    print("Sending alien structure packets...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 1337 bytes stands out mathematically.
    weird_size_packet = b"A" * 1337 
    for _ in range(25):
        sock.sendto(weird_size_packet, (TARGET_IP, PORT))
        time.sleep(0.05) 
    print("Anomaly traffic generation complete.")

if __name__ == "__main__":
    while True:
        print("\n" + "#"*30)
        print("   UCDS EXTERNAL ATTACK SIMULATOR")
        print("#"*30)
        print("1. Fire SQL Injection (SQLi)")
        print("2. Fire Cross-Site Scripting (XSS)")
        print("3. Fire Volumetric DDoS")
        print("4. Fire Zero-Day Anomaly (Trigger AI)")
        print("5. Exit")
        
        choice = input("\nSelect an attack to launch (1-5): ")
        if choice == '1': simulate_sqli()
        elif choice == '2': simulate_xss()
        elif choice == '3': simulate_ddos()
        elif choice == '4': simulate_ai_anomaly()
        elif choice == '5': break