import dns.reversename
domain_str = '164.4.217.172.in-addr.arpa.'
# Convert the string to a dns.name.Name object
domain_name = dns.name.from_text(domain_str)
ip = dns.reversename.to_address(domain_name)
print(ip)