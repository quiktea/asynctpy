# asynctpy
An asynchronous wrapper for the Tenor API written in Python

[![Discord][7]][8]

Getting Started:
Simply run the following command within your terminal (a PyPi release is coming soon):
```
pip install git+https://github.com/quiktea/asynctpy.git
```

Basic Usage:
```py
from asynctpy import AsyncTPY

tenor = AsyncTPY()
tenor.create_instance("tenor_api_key")

#search for a gif
async def foo():
  data = await tenor.search("cats", limit = 10)
  print(data)

#get a random gif
async def foo():
  data = await tenor.random("cats", limit = 10) #gets 10 gifs and chooses a random one out of them
  print(data)

#get more than one random gif
async def foo():
    data = await tenor.random_many("cats", 8, limit = 10) #gets 10 gifs and chooses 8 random ones from them
    print(data)

```

Coming Soon:
- Reusing one `aiohttp.ClientSession()` instead of just creating a new one every time
- Some Utils
- Something to remove unecessary characters within a search term




[8]: https://discord.com/api/guilds/815602429532962836/widget.json
[7]: https://discord.gg/jHt3qrNxyk