from scapy.all import sniff
from scapy.layers.inet import IP
import time
import random

latest_packet = {"protocol": 0, "length": 0, "ip": "Unknown"}
packet_count = 0
start_time = time.time()

# Try importing scapy
try:
    from scapy.all import sniff
    from scapy.layers.inet import IP
    SCAPY_AVAILABLE = True
except:
    SCAPY_AVAILABLE = False


def process_packet(packet):
    global latest_packet, packet_count
    if packet.haslayer(IP):
        latest_packet["protocol"] = packet[IP].proto
        latest_packet["length"] = len(packet)
        latest_packet["ip"] = packet[IP].src
        packet_count += 1


def capture_packet():
    global latest_packet

    if SCAPY_AVAILABLE:
        try:
            sniff(prn=process_packet, timeout=1)
        except:
            generate_dummy_packet()
    else:
        generate_dummy_packet()


def generate_dummy_packet():
    global latest_packet, packet_count

    protocols = ["TCP", "UDP", "ICMP"]
    latest_packet = {
        "protocol": random.choice(protocols),
        "length": random.randint(40, 1500),
        "ip": f"192.168.1.{random.randint(1,255)}"
    }
    packet_count += 1


def latest_packet_data():
    return latest_packet


def get_packet_rate():
    global packet_count, start_time
    elapsed = time.time() - start_time
    if elapsed == 0:
        return 0
    return round(packet_count / elapsed, 2)