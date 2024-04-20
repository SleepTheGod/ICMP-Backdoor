from scapy.all import *
import base64

def send_icmp_data(target_ip, data, chunk_size=10):
    # Base64 encode the data to ensure transmission of binary safe text
    encoded_data = base64.b64encode(data.encode())
    
    # Split data into chunks
    chunks = [encoded_data[i:i + chunk_size] for i in range(0, len(encoded_data), chunk_size)]
    
    for chunk in chunks:
        # Craft the packet with the ICMP data payload
        pkt = IP(dst=target_ip)/ICMP(type=8)/Raw(load=chunk)
        send(pkt)
        print(f"Sent: {chunk.decode()}")

message = "Hello, world! This is an ICMP test message."
target = "192.168.1.100"  # Change to the receiver's IP address
send_icmp_data(target, message)
