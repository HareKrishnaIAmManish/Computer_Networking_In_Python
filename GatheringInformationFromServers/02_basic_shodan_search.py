import shodan
import os

shodan_api_key=''
shodan=shodan.Shodan(shodan_api_key)
try:
    resultados=shodan.search('nginx')
    print(resultados)
    # print("results: ",resultados.items())
except Exception as e:
    print(str(e))    