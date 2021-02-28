import aiohttp
import random
import asyncio

async def create_session():
    async with aiohttp.ClientSession() as session:
        return session


class AsyncTPY():
    api_key = None
        

    @classmethod
    def create_instance(cls, token : str):
        cls.api_key = token

    @classmethod
    async def search(cls, search_term : str, limit : int = 8) -> dict:
        url = "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, cls.api_key, limit)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                
                return data

    @classmethod
    async def random(cls, search_term : str, limit : int = 8) -> dict:
        url = "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, cls.api_key, limit)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                results = data["results"]
                entry = random.choice(results)
                return entry

    @classmethod
    async def random_many(cls, search_term : str, results : int, limit : int = 8) -> list:
        if limit < results:
            raise ValueError("limit must not be smaller than results value")
        url = "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, cls.api_key, limit)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                returned_results = data["results"]
                return_list = []
                for _ in range(results):
                    entry = random.choice(returned_results)
                    return_list.append(entry)
                    returned_results.remove(entry)
                
                return return_list


tenor = AsyncTPY()
tenor.create_instance("LIVDSRZULELA")


async def main():
    data = await tenor.search("cats")
    print(data)


asyncio.get_event_loop().run_until_complete(main())