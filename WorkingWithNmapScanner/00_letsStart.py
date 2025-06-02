import nmap
print(nmap.__version__)
#nmap -sT target       tcp connect scan
"""
Step 1 (SYN): In the first step, the client wants to establish a connection with a server, so it sends a segment with SYN(Synchronize Sequence Number) which informs the server
 that the client is likely to start communication and with what sequence number it starts segments with
Step 2 (SYN + ACK): Server responds to the client request with SYN-ACK signal bits set. Acknowledgement(ACK) signifies the response of the segment it received 
and SYN signifies with what sequence number it is likely to start the segments with
Step 3 (ACK): In the final part client acknowledges the response of the server and they both establish a reliable connection with which they will start the actual
 data transfer
"""
#nmap sS target       tcp stealth scan 
"""
half tcp handshake
syn syn-ack
syn rst
"""
#nmap sU target       UDP scan
"""
udp packet sent and got udp port open
udp packet sent got icmp packet of type 3 port closed
"""
#nmap sA            TCP ACK Scan
"""
helps to know if a firewall is running
packet with ACK flag activated is sent if in return you get 
packet with RST flag activated it can be determined that
port is not filtered........... else if we dont get a response 
else if if we get a response with an ICMP packet it means a firewall
is filtering
"""
#nmap sN TCP NULL Scan
"""
tcp packet without any flag is sent if in respone we got then port is 
open or else we get rst flag port is closed 
"""
#nmap sF  TCP FIN Scan     FIN-> finish
"""
TCP packet with the FIN flag is sent if we get a response
then port is open else if we get RST flag port is closed
"""
#nmap sX     TCP XMAS Scan
"""
tcp packets with flag PSH FIN or URG is sent if remote machine
return a valid response port is open else if we get a RST flag then
port is closed else we get a ICMP type 3 message we say port is filtered
"""
