 # 1. objetivo - criar um API que vc manda 'game' ele retorna pong.
 # 2. URL base - localhost 
 # 3. Endpoints-
     #  - localhost/game (GET)
     #  - localhost/game (POST)
     #  -localhost/game/id (GET)
     #  -localhost/game/id (PUT)
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
@app.route('/game')
def obter_game():
    return jsonify(game)



app.run(port=5000,host='localhost',debug=True)