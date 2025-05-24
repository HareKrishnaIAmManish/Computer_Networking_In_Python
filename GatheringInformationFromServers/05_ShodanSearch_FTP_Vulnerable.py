import shodan
servers=[]
shodan_api_key='jmC3h0DQvdJIcfBIoKxkKMuI8HO5SPa5'
shodanApi=shodan.Shodan(shodan_api_key)
results=shodanApi.search("port:21 Anonymous user logged in")
print("hosts number: " + str(len(results['matches'])))
for result in results['matches']:
    if result['ip_str'] is not None:
        servers.append(result['ip_str'])
for server in servers:
    print(server)

