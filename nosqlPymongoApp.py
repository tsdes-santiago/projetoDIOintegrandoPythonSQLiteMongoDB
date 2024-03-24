from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pprint

uri = "<insira aqui a uri do seu usuário do MongoDB Atlas>"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Carregando o banco de dados 
db = client.test

print(db.list_collection_names())
# Carregando a coleção
collection = db.bank

pprint.pprint(collection.find_one())

"""
print('#'*100)
print("Lista de clientes")
print('#'*100)
for client in collection.find():
    pprint.pprint(client)
"""

print('#'*100)
print("Número de clientes")
print('#'*100)
print(collection.count_documents({}))

print('#'*100)
print("Lista de clientes ordenada")
print('#'*100)
for client in collection.find({}).sort("nome"):
    pprint.pprint(client)

print('#'*100)
print("Clientes com saldo > 2000")
print('#'*100)

for cliente in collection.find({"contas.saldo": {"$gt": 2000.00}}):
    print(f"Nome: {cliente['nome']}")
    for conta in cliente['contas']:
        print(f"    Conta: {conta['tipo']} - Saldo: R${conta['saldo']:.2f}")

print('#'*100)
print("Clientes com conta poupança")
print('#'*100)

for cliente in collection.find({"contas.tipo": "poupança"}):
    print(f"Nome: {cliente['nome']}")
    for conta in cliente['contas']:
        print(f"    Conta: {conta['tipo']} - Saldo: R${conta['saldo']:.2f}")