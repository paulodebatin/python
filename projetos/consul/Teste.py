import consul
import json

c = consul.Consul()

chave = "produto_1"
produto = {
    "id": 1,
    "descricao": "Caneta",
    "preco": 10.32,
    "quantidade": 123
}
c.kv.put(chave, json.dumps(produto, indent=2))

index, data = c.kv.get(chave)

produto = json.loads(data['Value'])
print(produto["id"])
print(produto["descricao"])
print(produto["preco"])
print(produto["quantidade"])

