import aiohttp


class Fetcher:
    @staticmethod
    async def get(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.text()

    @staticmethod
    async def delete(url):
        async with aiohttp.ClientSession() as session:
             async with session.delete(url) as resp:
                 return await resp.text()

    @staticmethod
    async def post(url, datas):
         async with aiohttp.ClientSession() as session:
             async with session.post(url, json=datas) as resp:
                 return await resp.text()