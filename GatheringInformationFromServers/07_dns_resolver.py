import dns.resolver
#hosts = ["oreilly.com", "yahoo.com", "google.com", "microsoft.com", "cnn.com"]
hosts=["www.iitism.ac.in"]
for host in hosts:
    print(host)
    # ip=dns.resolver.query(host,'A')
    ip=dns.resolver.resolve(host,'A')
    for i in ip:
        print(i)
