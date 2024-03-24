from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy import create_engine, inspect, select, func

Base = declarative_base()


class Cliente(Base):
    
    __tablename__ = 'clientes'

    # Atributos

    id = Column(Integer, primary_key = True)
    fullname = Column(String)
    cpf = Column(Integer)
    endereco = Column(String)

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Cliente(id={self.id:d}, name={self.fullname:s}, \
                 cpf={self.cpf:d}, endereco={self.endereco:s})>"


class Conta(Base):
    
    __tablename__ = 'contas'

    # Atributos

    id = Column(Integer, primary_key = True)
    tipo = Column(String)
    agencia = Column(Integer)
    numero = Column(Integer, unique=True)
    saldo = Column(Float)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"<Conta(id={self.id:d}, tipo={self.tipo:s}, agencia={self.agencia:d}, \
                numero={self.numero:d}, saldo={self.saldo:.2f}, cliente_id={self.cliente_id})>"

#print(Cliente.__tablename__)
#print(Conta.__tablename__)

# Conexão com o banco de dados

engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Investiga o esquema do banco de dados
inspetor = inspect(engine)

print('table names: ', inspetor.get_table_names())
print('default schema: ', inspetor.default_schema_name)

# Populando o banco de dados
with Session(engine) as session:
    
    # Clientes

    cliente1 = Cliente(
        fullname="João Silva",
        cpf=1234567890,
        endereco="joaosilva@email.com",
        conta=[
            Conta(
                tipo="corrente",
                agencia= 1,
                numero=123456,
                saldo=1000.00,
            ),
        ],
    )

    cliente2 = Cliente(
        fullname="Maria Oliveira",
        cpf=9876543210,
        endereco="mariaoliveira@email.com",
        conta=[
            Conta(
                tipo="poupança",
                agencia= 1,
                numero=2345670,
                saldo=500.00,
            ),
        ],
    )

    cliente3 = Cliente(
        fullname="Pedro Souza",
        cpf=1122334455,
        endereco="pedrosouza@email.com",
        conta=[
            Conta(
                tipo="corrente",
                agencia= 1,
                numero=345678,
                saldo=2000.00,
            ),
        ],
    )

    cliente4 = Cliente(
        fullname="Ana Costa",
        cpf=2233445566,
        endereco="anacosta@email.com",
        conta=[
            Conta(
                tipo="poupança",
                agencia=1,
                numero=4567890,
                saldo=1500.00,
            ),
        ],
    )

    cliente5 = Cliente(
        fullname="Carlos Santos",
        cpf=3344556677,
        endereco="carloshsantos@email.com",
        conta=[
            Conta(
                tipo="corrente",
                agencia=1,
                numero=567890,
                saldo=3000.00,
            ),
        ],
    )

    cliente6 = Cliente(
        fullname="Mariana Silva",
        cpf=4455667788,
        endereco="marianasilva@email.com",
        conta=[
            Conta(
                tipo="corrente",
                agencia=1,
                numero=678901,
                saldo=4000.00,
            ),
            Conta(
                tipo="poupança",
                agencia=1,
                numero=6789010,
                saldo=2500.00,
            ),
        ],
    )

    cliente7 = Cliente(
        fullname="Bruno Oliveira",
        cpf=5566778899,
        endereco="brunooliveira@email.com",
        conta=[
            Conta(
                tipo="corrente",
                agencia=1,
                numero=789012,
                saldo=5000.00,
            ),
        ],
    )

    cliente8 = Cliente(
        fullname="Camila Costa",
        cpf=6677889900,
        endereco="camilacosta@email.com",
        conta=[
            Conta(
                tipo="poupança",
                agencia=1,
                numero=8901230,
                saldo=3500.00,
            ),
        ],
    )

    cliente9 = Cliente(
        fullname="Daniel Santos",
        cpf=7788990011,
        endereco="danielsantos@email.com",
        conta=[
            Conta(
                tipo="corrente",
                agencia=1,
                numero=901234,
                saldo=6000.00,
            ),
        ],
    )

    cliente10 = Cliente(
        fullname="Fernanda Silva",
        cpf=8899001122,
        endereco="fernandasilva@email.com",
        conta=[
            Conta(
                tipo="corrente",
                agencia=1,
                numero=12345,
                saldo=7000.00,
            ),
        ],
    )
    # Enviando para o banco de dados (persistência de dados)
    session.add_all([eval(f'cliente{i}') for i in range(1,11)])

    session.commit()

# Consultas aos dados

statement = select(Cliente).where(Cliente.fullname.in_(["Camila Costa"]))

for cliente in session.scalars(statement):
    print(cliente)

statement = select(Conta).where(Conta.tipo.in_(['poupança']))
print('#'*100)
print('Contas tipo poupança')
print('#'*100)
for conta in session.scalars(statement):
    print(conta)
print('#'*100)

statement = select(Conta).where(Conta.saldo > 3000)

print('#'*100)
print('Contas Saldo > 3000')
print('#'*100)
for conta in session.scalars(statement):
    print(conta)

statement = select(Cliente).order_by(Cliente.fullname.desc())

print('#'*100)
print('Nomes clientes ordenados')
print('#'*100)
for cliente in session.scalars(statement):
    print(cliente)

print('#'*100)
print('Total clientes')
print('#'*100)
statement = select(func.count('*')).select_from(Cliente)
for cliente in session.scalars(statement):
    print(cliente)
