import aiohttp
import asyncio
import random
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) #aiohttp.ClientSession() requires you to create a session within an async context manager.
#To use one session, we cannot do this, so we are just going to ignore the warning :)

class AsyncTPY():
    api_key = None
    session = None #created within __init__

    
    
    @classmethod
    def create_instance(cls, token : str):
        cls.api_key = token
        cls.session = aiohttp.ClientSession(raise_for_status=True)

    @classmethod
    async def search(cls, search_term : str, limit : int = 8) -> dict:
        url = "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, cls.api_key, limit)
        async with cls.session.get(url) as response:
            data = await response.json()
            await cls.session.close()
            return data

    @classmethod
    async def random(cls, search_term : str, limit : int = 8) -> dict:
        url = "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, cls.api_key, limit)
        async with cls.session.get(url) as response:
            data = await response.json()
            results = data["results"]
            entry = random.choice(results)
            return entry

    @classmethod
    async def random_many(cls, search_term : str, results : int, limit : int = 8) -> list:
        if limit < results:
            raise ValueError("limit must not be smaller than results value")
        url = "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, cls.api_key, limit)
        async with cls.session.get(url) as response:
            data = await response.json()
            returned_results = data["results"]
            return_list = []
            for _ in range(results):
                entry = random.choice(returned_results)
                return_list.append(entry)
                returned_results.remove(entry)
                
            return return_list


    @classmethod
    async def destroy_instance(cls):
        await cls.session.close()
        





