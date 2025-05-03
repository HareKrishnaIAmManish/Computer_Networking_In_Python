import argparse
import subprocess
import sys
parser=argparse.ArgumentParser(description="Ping Scan Network")
parser.add_argument("-network",dest="network",help="Network segment [like 192.127.25.21]",required=True)
parser.add_argument("-machines",dest="machines",help="Machine Number",type=int,required=True)
parsed_args=parser.parse_args()
for ip in range (1,parsed_args.machines+1):
    ipAdress=parsed_args.network+'.'+str(ip)
    print("scanning %s"%ipAdress)
    if sys.platform.startswith('linux'):
      output=subprocess.Popen(['/bin/ping','-c 1',ipAdress],stdout=subprocess.PIPE).communicate()[0]
    elif sys.platform.startswith('win'):
      output = subprocess.Popen(['ping', ipAdress], stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()[0]
    output = output.decode('utf-8')
    print("Output",output)
    if "Lost = 0" in output or "bytes from " in output:
        print("The Ip Address %s has responded with a ECHO_REPLY!" % ipAdress)
        