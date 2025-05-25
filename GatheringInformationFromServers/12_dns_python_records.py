import dns.resolver
def main(domain):
    records=['A','AAAA','NS','SOA','MX','TXT']
    for record in records:
        try:
            responses=dns.resolver.query(domain,record)
            print("\nRecord response ",record)
            print('------------------------------------')
            for response in responses:
                print(response)
        except Exception as e:
            print('cant resolve query for record ',record)
            print('Error for obtaining record information: ',e)
if __name__=='__main__':
    try:
        main('ark.iitism.ac.in')
    except KeyboardInterrupt:
        exit()                