from shlex import quote
filename='somefile; rm -rf -'
command='ls-l {}'.format(quote(filename)) #secure
print(command)
