from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml
from flask_marshmallow import Marshmallow


app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Produto(db.Model):
    __tablename__ = "produto"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)


class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produto
        sqla_session = db.session
        load_instance = True        