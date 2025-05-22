import httpx
import asyncio
async def request_http1():
    async with httpx.AsyncClient() as client:
        response=await client.get("http://www.goole.es")
        print(response)
        print(response.text)
        print(response.http_version)
asyncio.run(request_http1())      
