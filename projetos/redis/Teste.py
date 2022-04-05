# Para maiores informaçções: 
# https://kb.objectrocket.com/redis/redis-example-with-python-951
# https://realpython.com/python-redis/

import redis
import json
redis = redis.Redis(host='localhost', port=6379)

chave = "produtos#1"
produto = {
    "id": 1,
    "descricao": "Caneta",
    "preco": 10.32,
    "quantidade": 123
}
redis.set(chave, json.dumps(produto, indent=2))

produto = json.loads(redis.get(chave)["Value"])
print(produto["id"])
print(produto["descricao"])
print(produto["preco"])
print(produto["quantidade"])

