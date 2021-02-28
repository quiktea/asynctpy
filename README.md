# asynctpy
An asynchronous wrapper for the Tenor API written in Python

[![Discord][7]][8]
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

[7]: https://media.discordapp.net/attachments/773312837623218247/815606365653303296/dlogo.png
[8]: https://discord.gg/jHt3qrNxyk