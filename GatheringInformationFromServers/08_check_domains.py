import argparse
import dns.name
def main(domain1,domain2):
    print("domain 1 is ",domain1)
    print("domain 2 is ",domain2)
    domain1=dns.name.from_text(domain1)
    domain2=dns.name.from_text(domain2)
    print("domain 1 is ",domain1)
    print("domain 2 is ",domain2)
    print("domain1 is subdomain of domain2",domain1.is_subdomain(domain2))
    print("domain2 is subdomain of domain1",domain2.is_subdomain(domain1)) 
if __name__ =='__main__':
    parser=argparse.ArgumentParser(description="check two domains with dns python")
    parser.add_argument('--domain1',action="store",dest="domain1",default='python.org')
    parser.add_argument('--domain2',action="store",dest="domain2",default="docs.python.org")
    given_args=parser.parse_args()
    domain1=given_args.domain1
    domain2=given_args.domain2
    main(domain1,domain2)

