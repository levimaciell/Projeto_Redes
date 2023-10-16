from flask import Flask, request, jsonify
import uuid
import sys
import json

sys.path.append('objects/')
from mensagem import Mensagem, serializar
from usuario import Usuario, serializarUsuario

app = Flask(__name__)

#Dicionário de usuários...
dadosUser = {"usuarios":[]}

#Dicionário de mensagens...
dados = {"mensagens":[]}

def isInUsers(nome):
    for n in dadosUser['usuarios']:
        if(n) == nome:
            return True
    
    return False

@app.route('/enviar', methods=['POST'])
def enviar():

    msg = request.json.get('mensagem')
    usuario = request.json.get('usuario')
    usuarioFinal = request.json.get('usuarioFinal')

    if msg:
        #Adicionando obj Mensagem
        dados["mensagens"].append(Mensagem(uuid.uuid4(), msg, usuario, usuarioFinal))
        print("\nMensagem Recebida: " + msg)
        return jsonify({'status': 'Mensagem enviada'}), 200
    return jsonify({'status': 'Erro ao enviar mensagem'}), 400

@app.route('/receber', methods=['GET'])
def receber():
    #Transformando dict em um json
    return json.dumps(dados, default=serializar)

@app.route('/usuario', methods=['POST'])
def criarUsuario():

    nome = request.json.get('nome')

    if nome != "" and not isInUsers(nome):
        user = Usuario(uuid.uuid4(), nome)
        dadosUser['usuarios'].append(user)
        print(f"\nNovo usuário adicionado: {user}")
        return jsonify({'status': 'Usuário criado com sucesso'}), 200
    return jsonify({'status':'Erro ao criar usuário!'}), 400

@app.route('/usuario', methods=['GET'])
def listarUsuarios():
    return json.dumps(dadosUser, default=serializarUsuario)



if __name__ == '__main__':
    app.run(debug=True, port=5555)


#TODO Exiba na tela cada mensagem recebida (FEITO)
#TODO Adicione um número único (id) para cara mensagem (FEITO)
#TODO Tenha como parâmetro um valor de mensagem para retornar apenas as mensagens deste id em diante 
