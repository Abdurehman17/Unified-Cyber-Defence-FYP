# 🛡️ Unified Cyber Defense Solution (UCDS)

A custom-built, Python-based Intrusion Prevention System (IPS) that integrates Deep Packet Inspection (DPI) with an Isolation Forest Machine Learning model. Designed to bridge the gap between traditional rule-based firewalls and autonomous AI threat hunting.

This project was developed as a Final Year Project for a BS in Cybersecurity.

## 🚀 Features

- **Real-Time Deep Packet Inspection (DPI):** Utilizes `Scapy` to parse raw network traffic at the application layer.
- **Dual-Engine Architecture:** Dynamically routes traffic between a signature-based engine and a behavioral AI engine to prevent "Rule Shadowing."
- **Zero-Day Anomaly Detection:** Employs an **Isolation Forest ML model** (`scikit-learn`) to establish a mathematical baseline of standard network traffic and instantly isolate structural anomalies without relying on known signatures.
- **Volumetric Attack Mitigation:** Custom counters detect and block rapid Port Scans and UDP-based DDoS floods.
- **Application-Layer Defense:** Actively inspects payloads for malicious strings, blocking SQL Injection (SQLi) and Cross-Site Scripting (XSS) attempts.
- **Automated Firewall Integration:** Interfaces directly with the Windows host OS to automatically drop malicious IPs in real-time.

## 🧠 The Architecture: Handling Rule Shadowing

One of the core engineering challenges of UCDS is preventing the AI from falsely flagging high-speed attacks (like DDoS) as "behavioral anomalies," which masks the true nature of the threat.

UCDS solves this using **Pre-emptive Flood Routing**. The system tracks elapsed time and packet frequency; if a volumetric flood is detected building up, the engine explicitly bypasses the AI, allowing the DDoS rule to properly categorize and mitigate the attack.

## 🛠️ Technology Stack

- **Backend:** Python 3.14.6
- **Packet Sniffing:** Scapy
- **Machine Learning:** Scikit-Learn (Isolation Forest), NumPy
- **Web Dashboard:** Flask (REST API)
- **Simulation:** Python `socket` programming for the multi-vector attack script

## 📦 Installation

**Clone the repository:**

```bash
git clone https://github.com/Abdurehman17/UCDS.git
cd UCDS
```

**Install required dependencies:**

```bash
pip install -r requirements.txt
```

> **Note:** Ensure you have `scapy`, `flask`, `psutil`, `fpdf`, `scikit-learn`, and `requests` installed.

**Run the application:**

Because packet sniffing requires root privileges, you must run the app as Administrator or using `sudo`:

```bash
sudo python3 backend/app.py
```

## 💻 Usage (Two-Machine Setup)

For accurate results that mimic a real-world Security Operations Center (SOC), a two-machine setup is recommended to avoid OS-level loopback interference.

### On the Defense Machine

1. Navigate to the `backend/` directory.
2. Start the server:
```bash
   python app.py
```
3. Open the web dashboard and click **Start Monitoring**.
4. Generate standard background traffic (e.g., browsing the web) for a few seconds to allow the AI to establish a baseline. Wait for the `[AI ENGINE] Training Complete!` terminal prompt.

### On the Attack Machine

1. Open `Testing_Attacks/run_tests.py`.
2. Update the `TARGET_IP` variable to the IP address of the Defense Machine.
3. Launch the simulator:
```bash
   python run_tests.py
```
4. Select an attack vector (SQLi, XSS, DDoS, or Zero-Day Anomaly) and watch the UCDS dashboard block the threat in real-time.

### Access the Dashboard

Open your web browser and navigate to `http://127.0.0.1:5000`.

## ⚠️ Disclaimer

This tool was developed as a Final Year Project (FYP) for educational and research purposes only. Do not use this tool on networks you do not have explicit permission to monitor.
