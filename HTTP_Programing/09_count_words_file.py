import urllib.request
import urllib.error
def count_words_file(url):
    try:
        file_response=urllib.request.urlopen(url)
    except urllib.error.URLError as error:
        print('Exception',error)
        print('reason',error.reason)
    else:
        content=file_response.read()
        return len(content.split()) 
print(count_words_file('https://cars.tatamotors.com/safari/ice.html')) 
count_words_file('https://not-exists.txt')
