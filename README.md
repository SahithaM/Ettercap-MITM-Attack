# Ettercap-MITM-Attack
This is a networking and cybersecurity lab project focused on ARP cache poisoning, traffic sniffing using Wireshark, and TCP reset spoofing using Scapy (Python). It demonstrates how to intercept and disrupt FTP/SSH traffic in a switched environment using man-in-the-middle (MITM) techniques.

---

## 🛠 Tools Used

- **Kali Linux** – Attacking machine
- **Ubuntu Linux** – Victim machine
- **Metasploitable 2** – Target FTP/SSH server
- **Ettercap** – ARP spoofing and MITM attacks ([GitHub](https://github.com/Ettercap/ettercap))
- **Wireshark** – Packet analysis ([Filters Guide](https://wiki.wireshark.org/DisplayFilters))
- **Scapy (Python)** – TCP reset injection ([Documentation](https://scapy.readthedocs.io/en/latest/))
- **VM Ware Workstation Pro** – VM networking

---

## 🎯 Objectives

- Perform ARP cache poisoning using Ettercap
- Intercept FTP login credentials using Wireshark
- Understand why passive sniffing fails in switched networks
- Use Scapy to spoof TCP Reset packets and terminate sessions

---

## 📂 Files

- `tcp_reset.py` – Python script used to inject TCP RST packets
- `ettercap_config_notes.txt` – Key installation and configuration commands
- `Lab_Report_Sahitha_Medasani.pdf` – Step-by-step walkthrough and screenshots
- `screenshots/` – Folder containing key output visuals

---

## 🧩 Lab Steps Summary

### 🔹 Step 1: Environment Setup
- Switched to root user: `sudo su -`
- Installed Ettercap build dependencies.
- Cloned Ettercap from GitHub and built it from source.
- Edited `/etc/ettercap/etter.conf` to set `ec_uid = 0` and `ec_gid = 0`
- Enabled IP forwarding:  
  `sudo sysctl -w net.ipv4.ip_forward=1`
- Installed FTP on Kali Linux.

### 🔹 Step 2: Packet Sniffing with Wireshark
- Ran Wireshark on Kali.
- Connected to FTP server at `192.168.86.21` via `ftp`.
- Used filter:  
  `tcp and ip.dst==192.168.86.21`
- Intercepted username/password via TCP stream.

### 🔹 Step 3: Sniffing Other Users' FTP Traffic
- Tried sniffing traffic from Ubuntu to Metasploitable.
- No packets captured during this step.

### 🔹 Step 4: ARP Spoofing Attack with Ettercap
- Launched Ettercap GUI.
- Scanned for hosts and added Ubuntu and Metasploitable as Target 1 and 2.
- Successfully sniffed credentials during FTP from Ubuntu.

### 🔹 Step 5: TCP Reset Attack with Python (Scapy)
- Wrote a Python script to send TCP RST packets to disrupt a session.
- Successfully ran the attack.

---

## 📸 Screenshots

| File Name | Description |
|-----------|-------------|
| `ettercap_host_scan.png` | Ettercap scanning the network for hosts |
| `ettercap_targets_set.png` | Targets set: Ubuntu and Metasploitable 2 |
| `ettercap_poisoning_active.png` | ARP poisoning successfully started |
| `wireshark_before_mitm.png` | Wireshark showing no traffic before MITM |
| `wireshark_tcp_stream.png` | Captured FTP credentials (user/password) |
| `ubuntu_ftp_reset.png` | FTP session terminated after TCP reset |
| `ssh_reset_attack.png` *(optional)* | SSH session disruption  |

---

## 🧠 Observations

- Passive sniffing in a switched environment does not capture traffic between other hosts.
- ARP cache poisoning allows the attacker to become the MITM and intercept credentials.
- TCP reset packets crafted with Scapy can forcefully terminate FTP and SSH sessions.

---

## 👩‍💻 Author

**Sahitha Medasani**  
[LinkedIn](https://www.linkedin.com/in/sahithamedasani/)
