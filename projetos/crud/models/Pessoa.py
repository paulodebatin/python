from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Pessoa(db.Model):
    __tablename__ = "pessoa"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    endereco = db.Column(db.String(255))
    numero = db.Column(db.String(20))
    bairro = db.Column(db.String(255))
    cidade = db.Column(db.String(255))
    uf = db.Column(db.String(2))
    receber_noticias = db.Column(db.Boolean)
    fumante =  db.Column(db.Boolean)
    cep = db.Column(db.String(8))
    data_nascimento = db.Column(db.Date)
    
    

class PessoaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pessoa
        sqla_session = db.session
        load_instance = True    