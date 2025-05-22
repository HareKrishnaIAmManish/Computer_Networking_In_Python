import requests
http_proxy="http://<ip_address>:<port>"
proxy_dictionary={"http":http_proxy}
requests.get("http://domain.com",proxies=proxy_dictionary)
