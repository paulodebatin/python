## Para maiores informações, consultar: 
# https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/connecting.html
# https://docs.objectrocket.com/elastic_python_examples.html


from elasticsearch import Elasticsearch
es = Elasticsearch(["http://localhost:9200"])


# Cria/atualiza
doc = {
    'descricao': 'Caneta',
    'preco': 11.11,
    'quantidade': 123,
}
res = es.index(index="produtos", id=1, body=doc)


# Recupera
res = es.get(index="produtos", id=1)
print(res['_source']["descricao"])
print(res['_source']["preco"])
print(res['_source']["quantidade"])

