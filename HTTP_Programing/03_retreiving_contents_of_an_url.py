from urllib.request import urlopen
# response=urlopen('http://www.iitism.ac.in/')
# print(urllib.request.urlopen("http://packtpub.com",timeout=30))
response=urlopen('http://web.simmons.edu/~grovesd/comm244/notes/week2/links')
print(response)
print(response.readline())
print(response.read())