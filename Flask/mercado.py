"""
 - Instalação do Ambiente Virtual:
> Instalar ambiente virtual: python -m venv .venv
> Activar o ambiente: .\.venv\Scripts\activate

- Instalação do Flask
> pip install flask

- Verificar a versão
> flask --version

- Ligar servidor com debug
> flask --app mercado run --debug

- Documentação do Flask SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/
- Pip Install: https://pypi.org/project/Flask-SQLAlchemy/
- Para rodar postgre é necesário o pacote: pip install sqlalchemy psycopg2

! Se der problemas com a instalação precione CRTL + SHIFT + P > digita Python > Python Interpretador > Escolha a versão da máquina
"""

from flask import Flask, render_template
import sqlalchemy
from sqlalchemy.orm import registry, sessionmaker
from sqlalchemy import Column, Integer, String, MetaData, Table


app = Flask(__name__)

# Conectando ao banco de dados
db_user = "postgres"
db_password = "vitor987sa%40A"
db_host = "localhost"
db_name = "geoprocess"
db_schema = 'public'

connection_string = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

engine = sqlalchemy.create_engine(connection_string, echo=True)

# Declarando o mapeamento
metadata = MetaData()
mapper_registry = registry()

@mapper_registry.mapped
class Region:
    __tablename__ = Table('region', mapper_registry.metadata, autoload_with=engine)
    region_id = Column(Integer, primary_key=True)
    region_description = Column(String(60))

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def hello_world():
    regions = session.query(Region).all()
    return render_template("home.html", regions = regions)

@app.route('/sobre/<usuario>')
def sobre(usuario):
    return f"<h3> Sobre mim: {usuario}</h3>"