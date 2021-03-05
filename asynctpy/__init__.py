import aiohttp
import asyncio
import random
import warnings
from utils.stringcleaner import clean_string
warnings.filterwarnings("ignore", category=DeprecationWarning) #aiohttp.ClientSession() requires you to create a session within an async context manager.
#To use one session, we cannot do this, so we are just going to ignore the warning :)

class AsyncTPY():
    
    def __init__(self, token : str):
        self.api_key = token
        self.session = aiohttp.ClientSession(raise_for_status=True)
    
    
    

    async def search(self, search_term : str, limit : int = 8) -> dict:
        search_term = await clean_string(search_term)
        url = "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, self.api_key, limit)
        async with self.session.get(url) as response:
            data = await response.json()
            return data

    async def random(self, search_term : str, limit : int = 8) -> dict:
        search_term = await clean_string(search_term)
        url = "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, self.api_key, limit)
        async with self.session.get(url) as response:
            data = await response.json()
            results = data["results"]
            entry = random.choice(results)
            return entry

    async def random_many(self, search_term : str, results : int, limit : int = 8) -> list:
        if limit < results:
            raise ValueError("limit must not be smaller than results value")
        search_term = await clean_string(search_term)
        url = "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, self.api_key, limit)
        async with self.session.get(url) as response:
            data = await response.json()
            returned_results = data["results"]
            return_list = []
            for _ in range(results):
                entry = random.choice(returned_results)
                return_list.append(entry)
                returned_results.remove(entry)
                
            return return_list


    async def destroy_instance():
        await self.session.close()
        self.session = None
        self.api_key = None
        del self.session
        del self.api_key

        

