services={"smtp":25,"ssh":22,"ftp":21,"http":80,"mandy":2356987523}
print(services["mandy"])
services={"smtp":25,"ssh":22,"ftp":21,"http":80,"mandy":2356987523,"mandy":"baigan"}
print(services["mandy"])
dictionary1={"ssh":22,"ftp":21,"http":80,"smtp":25}
dictionary2={"ssh":22,"ftp":21,"ldap":389,"snmp":161}
print(dictionary1)
dictionary1.update(dictionary2)
print(dictionary1)
dictionary1["mandy"]="baigan"
print(dictionary1)
print(len(dictionary1))
# keys1=dictionary1.keys()
# print(keys1)
# print(type(keys1))
items1=dictionary1.items()
print(items1)
for k,v in items1:
    print("protocol is ",k," its port number is ", v)







