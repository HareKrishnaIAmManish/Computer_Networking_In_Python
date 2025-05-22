import httpx
import trio
# print(trio.__version__)
results={}
async def fetch_result(client,url,results):
    print(url)
    results[url]=await client.get(url)
async def main_pallarel_requests():
    async with httpx.AsyncClient(http2=True) as client:
        async with trio.open_nursery() as nursey:
            for i in range (2000,2020):
                url=f"https://en.wikipedia.org/wiki/{i}"
                nursey.start_soon(fetch_result,client,url,results)
trio.run(main_pallarel_requests)
print(results)