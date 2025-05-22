import httpx
import asyncio
async def request_http2():
    async with httpx.AsyncClient(http2=True) as client:
        response=await client.get("https://www.google.com")
        print(response)
        print(response.http_version)
        print(response.text)
asyncio.run(request_http2())
