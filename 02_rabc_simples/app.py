'''
Instlacao das dependencias:
pip install Flask 
pip install Flask-HTTPAuth
pip install python-json-config

Execucao:
python app.py

Exemplo de chamada:
ver lista de usuarios: curl --user id01:tom123 -i http://localhost:5000/api/v1/users 
criar usuario: curl --user id01:tom123 -i -H "Content-Type: application/json" -X POST -d '{"userId":"id03", "username": "joana","password":"1234","role":"Parent"}' http://localhost:5000/api/v1/user
'''


from flask import Flask, request, jsonify, abort
from flask_httpauth import HTTPBasicAuth
from python_json_config import ConfigBuilder

## Funcoes auxiliares ##
def getPerfil(users, username):
    for user in users:
        if(username == user["userId"]):
            return user

def autorizaUsuario(username, roles):
    user = getPerfil(apiProfile.users, username)
    print(user, roles)
    if user["role"] in roles:
        return True
    return False

# Inicializacao da api Flask ##
app = Flask(__name__)
app.config["DEBUG"] = True
auth = HTTPBasicAuth() 
builder = ConfigBuilder()
apiProfile = builder.parse_config('users.json')

## Rotas da API ##
@app.route('/', methods=['GET'])
def home():
    return "<h1> Home </h1>"

@app.route('/api/v1/users', methods=['GET'])
@auth.login_required
def api_users():
    return str(apiProfile.users)

@auth.verify_password
def verifica_senha(username, password):
    print("verifica")
    user = getPerfil(apiProfile.users, username)
    if(user == None):
        return False
    return password == user["password"]

@app.route('/api/v1/user', methods=['POST'])
@auth.login_required
def add_usuario():
    is_autorizado = autorizaUsuario(username=auth.username(), roles = apiProfile.actions.addUsers)
    if not is_autorizado:
        abort(403)
    payload = request.get_json()

    usuario = getPerfil(apiProfile.users, payload["userId"])
    if(usuario != None): abort(400, "Usuario ja existe")
    apiProfile.users.append(payload)
    configFile = open("users.json", "w")
    configFile.write(apiProfile.to_json())
    return "User created"

app.run()
