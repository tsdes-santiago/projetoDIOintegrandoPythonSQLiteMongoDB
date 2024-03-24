from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "<insira aqui a uri do seu usuário mongoDB Atlas>"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Criando o banco de dados
db = client.test
# Criando a coleção bank
collection = db.bank
print(db.bank)

# Dados para popular o banco de dados
dados_nosql = [
    {
        "nome": "João Silva",
        "cpf": 1234567890,
        "endereco": "joaosilva@email.com",
        "contas": [
            {
                "tipo": "corrente",
                "agencia": 1,
                "numero": 123456,
                "saldo": 1000.00,
            },
        ],
    },
    {
        "nome": "Maria Oliveira",
        "cpf": 9876543210,
        "endereco": "mariaoliveira@email.com",
        "contas": [
            {
                "tipo": "poupança",
                "agencia": 1,
                "numero": 234567,
                "saldo": 500.00,
            },
        ],
    },
    {
        "nome": "Pedro Souza",
        "cpf": 1122334455,
        "endereco": "pedrosouza@email.com",
        "contas": [
            {
                "tipo": "corrente",
                "agencia": 1,
                "numero": 345678,
                "saldo": 2000.00,
            },
        ],
    },
    {
        "nome": "Ana Costa",
        "cpf": 2233445566,
        "endereco": "anacosta@email.com",
        "contas": [
            {
                "tipo": "poupança",
                "agencia": 1,
                "numero": 456789,
                "saldo": 1500.00,
            },
        ],
    },
    {
        "nome": "Carlos Santos",
        "cpf": 3344556677,
        "endereco": "carloshsantos@email.com",
        "contas": [
            {
                "tipo": "corrente",
                "agencia": 1,
                "numero": 567890,
                "saldo": 3000.00,
            },
        ],
    },
    {
        "nome": "Mariana Silva",
        "cpf": 4455667788,
        "endereco": "marianasilva@email.com",
        "contas": [
            {
                "tipo": "corrente",
                "agencia": 1,
                "numero": 678901,
                "saldo": 4000.00,
            },
            {
                "tipo": "poupança",
                "agencia": 1,
                "numero": 6789010,
                "saldo": 2500.00,
            },
        ],
    },
    {
        "nome": "Bruno Oliveira",
        "cpf": 5566778899,
        "endereco": "brunooliveira@email.com",
        "contas": [
            {
                "tipo": "corrente",
                "agencia": 1,
                "numero": 789012,
                "saldo": 5000.00,
            },
            {
                "tipo": "poupança",
                "agencia": 1,
                "numero": 7890120,
                "saldo": 3000.00,
            },
        ],
    },
    {
        "nome": "Camila Costa",
        "cpf": 6677889900,
        "endereco": "camilacosta@email.com",
        "contas": [
            {
                "tipo": "poupança",
                "agencia": 1,
                "numero": 890123,
                "saldo": 3500.00,
            },
            {
                "tipo": "corrente",
                "agencia": 1,
                "numero": 8901230,
                "saldo": 4500.00,
            },
        ],
        },
        {
            "nome": "Daniel Santos",
            "cpf": 7788990011,
            "endereco": "danielsantos@email.com",
            "contas": [
                {
                    "tipo": "corrente",
                    "agencia": 1,
                    "numero": 901234,
                    "saldo": 6000.00,
                },
            ],
        },
        {
            "nome": "Fernanda Silva",
            "cpf": 8899001122,
            "endereco": "fernandasilva@email.com",
            "contas": [
                {
                    "tipo": "corrente",
                    "agencia": 1,
                    "numero": 112345,
                    "saldo": 7000.00,
                },
            ],
        },
    ]

# Preparando para submeter os dados
data_id = collection.insert_many(dados_nosql).inserted_ids

print(data_id)