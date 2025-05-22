import httpx
client=httpx.Client(timeout=10.0)
response=client.get("https://www.google.com")
print(response)
print(response.status_code)
print(response.text)
