from scapy.all import sniff

# quit playing on my top
def packet_callback(packet):
    print(packet.summary())

# Packet sniffing built in function
sniff(prn=packet_callback, count=10)
