 # 1. objetivo - criar um API que vc manda 'game' ele retorna pong.
 # 2. URL base - localhost 
 # 3. Endpoints-
     #  - localhost/game (GET)
     #  - localhost/game (POST)
     #  -localhost/game/PING (GET)
     #  -localhost/game/PONG (PUT)
     #  -localhost/game (DELETE)
 # 4. Quais recursos 
 
from flask import Flask, jsonify, request

app = Flask(__name__)

game = [
    {
        'cliente': 'play',
        'recebe': 'PING'
    }
]
 
#Consultar (todos)
@app.route('/game',methods=['GET'])
def obter_game():
    return jsonify(game)

#Consultar (PING)
@app.route('/game/<int:PING>',methods=['GET'])
def obter_game_por_PING(PING):
    for game in game:
       if game.get('PING') == PING:
           return jsonify(game)

#Editar
@app.route('game/<int:PING>',methods=['PUT'])
def editar_game_por_PING(PING):
    game_alterado = request.get_json()
    for indice,game in enumerate(game):
        if game.get('PING') == PING:
            game[indice].update(game_alterado)
            return jsonify(game[indice]) 

app.run(port=5000,host='localhost',debug=True)