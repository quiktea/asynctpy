# asynctpy
An asynchronous wrapper for the Tenor API written in Python


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

```