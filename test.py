import json
import urllib.request





poke_url = f"https://pokeapi.co/api/v2/pokemon"

poke_url = f"{ poke_url }/pikachu"

req = urllib.request.Request(
        url=poke_url,
        headers={"User-Agent": "Mozilla/5.0"}
        )

print(urllib.request.urlopen(req))

