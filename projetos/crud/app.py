from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models.Pessoa import Pessoa, PessoaSchema
from models.Produto import Produto, ProdutoSchema

import yaml

app = Flask(__name__)
db_config = yaml.load(open('database.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['uri'] 
db = SQLAlchemy(app)
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/pessoas', methods=['POST', 'GET'])
def pessoas():
    
    if request.method == 'POST':
        json_data = request.json

        pessoaSchema = PessoaSchema()
        data = pessoaSchema.load(json_data)

        db.session.add(data)
        db.session.commit()

        return pessoaSchema.dump(data)
    
    if request.method == 'GET':
        data = Pessoa.query.order_by(Pessoa.id).all()
        pessoaSchema = PessoaSchema(many=True)
        return jsonify(pessoaSchema.dump(data))   


@app.route('/pessoas/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def pessoa(id):

    if request.method == 'GET':
        data = Pessoa.query.get(id)
        pessoaSchema = PessoaSchema()
        return pessoaSchema.dump(data)

        
    if request.method == 'DELETE':
        delData = Pessoa.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({'status': 'ID:  '+id+' excluído!'})

    if request.method == 'PUT':
        editData = Pessoa.query.filter_by(id=id).first()

        json_data = request.json
        pessoaSchema = PessoaSchema()
        data = pessoaSchema.load(json_data)
        if  data.nome !=  None:
            editData.nome = data.nome
        if  data.endereco !=  None:
            editData.endereco = data.endereco
        if  data.numero !=  None:
            editData.numero = data.numero
        if  data.bairro !=  None:
            editData.bairro = data.bairro
        if  data.cidade !=  None:
            editData.cidade = data.cidade
        if  data.uf !=  None:
            editData.uf = data.uf
        if  data.cep !=  None:
            editData.cep = data.cep
        if  data.receber_noticias !=  None:
            editData.receber_noticias = data.receber_noticias
        if  data.fumante !=  None:
            editData.fumante = data.fumante
        if  data.data_nascimento !=  None:
            editData.data_nascimento = data.data_nascimento

        db.session.commit()
        return jsonify({'status': 'Id '+id+' atualizado!'})


@app.route('/produtos', methods=['POST', 'GET'])
def produtos():
    
    if request.method == 'POST':
        json_data = request.json

        produtoSchema = ProdutoSchema()
        data = produtoSchema.load(json_data)

        db.session.add(data)
        db.session.commit()

        return produtoSchema.dump(data)
    
    if request.method == 'GET':
        data = Produto.query.order_by(Produto.id).all()
        produtoSchema = ProdutoSchema(many=True)
        return jsonify(produtoSchema.dump(data))          



@app.route('/produtos/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def produto(id):

    if request.method == 'GET':
        data = Produto.query.get(id)
        produtoSchema = ProdutoSchema()
        return produtoSchema.dump(data)

        
    if request.method == 'DELETE':
        delData = Produto.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({'status': 'ID:  '+id+' excluído!'})

    if request.method == 'PUT':
        editData = Produto.query.filter_by(id=id).first()

        json_data = request.json
        produtoSchema = ProdutoSchema()
        data = produtoSchema.load(json_data)
        if  data.nome !=  None:
            editData.nome = data.nome
        if  data.preco !=  None:
            editData.preco = data.preco
        if  data.quantidade !=  None:
            editData.quantidade = data.quantidade

        db.session.commit()
        return jsonify({'status': 'Id '+id+' atualizado!'})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
