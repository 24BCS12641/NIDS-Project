from scapy.all import sniff
from scapy.layers.inet import IP
import time

latest_packet = {"protocol": 0, "length": 0}
packet_count = 0
start_time = time.time()

def process_packet(packet):
    global latest_packet, packet_count
    if packet.haslayer(IP):
        latest_packet["protocol"] = packet[IP].proto
        latest_packet["length"] = len(packet)
        packet_count += 1

def capture_packet():
    sniff(prn=process_packet, timeout=1)

def get_packet_rate():
    global packet_count, start_time
    elapsed = time.time() - start_time
    if elapsed == 0:
        return 0
    rate = packet_count / elapsed
    return round(rate, 2)