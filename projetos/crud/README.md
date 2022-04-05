# backend-python3

## Project setup  - Necessário ter instalado:
* Postgres instalado e iniciado (host: localhost:5432, usuário: postgres, senha: 123456, banco: vendas vazio)
Rodar os scripts da pasta scripts
Qualquer mudança neste endereço você precisa alterar no arquivo database.yaml 
* Python 3
* Bibliotecas utilizadas instaladas: Para instalar:
```
cd backend-python3
pip3 install flask flask_cors Flask-SQLAlchemy psycopg2 flask-marshmallow marshmallow-sqlalchemy marshmallow
```

### Para colocar no ar:

```
cd backend-python3
python3 app.py
```

Será iniciado na porta 3000. Ex.: GET  http://localhost:3000/pessoas

```bash
POST /pessoas
body request: {nome:"x", endereco:"y"}
```

```bash
GET /pessoas
GET /pessoas/{:id}
```

```bash
PUT /pessoas/{:id}
body request: {nome:"x", endereco:"y"}
```

```bash
DELETE /pessoas/{:id}
```

### Tecnologias utilizadas no projeto:
* Python 3
* Flask
* Psycopg2
* SQLAlchemy
* Marshmallow
* Postgres

### Melhorias que poderiam ser feitas:
* Separar as rotas de pessoas e produtos em arquivos separadas para não ficar apenas em um único arquivo
* Fazer validação nos endpoints 
* Criar classes de serviço e não chamar dentro da controller/endpoints a persistência dos dados
* Melhorar os mapeamentos das classes SQLAlchemy de Pessoa e Produto (campos obrigatórios, ...)
