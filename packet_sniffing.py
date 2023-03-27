from scapy.all import *

# Define the filter to capture only HTTP GET requests to example.com
filter_str = "tcp and host example.com"

# Define the callback function to process captured packets
def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        print(packet.show()) # Print the packet information

# Start capturing packets
sniff(filter=filter_str, prn=packet_callback)