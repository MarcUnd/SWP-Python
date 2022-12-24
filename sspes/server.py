from flask import Flask, request
from flask_restful import Resource, Api
import playerHandeling as ph
file = 'player_data.json'

app = Flask(__name__)
api = Api(app)


class PlayerRequests(Resource):
    def get(self, name):
        return ph.getPlayers(name, file)
    def post(self, name):
        return ph.create(name, file)
    def delete(self, name):
        return ph.delete(name, file)
    
    @app.route('/update', methods=['GET'])
    def doSomething():
        name = request.args.get('name')
        win = int(request.args.get('win'))
        choice = int(request.args.get('choice'))
        statsArr = [0,0,0]
        statsArr[win]=1
        return ph.updateStats(name, statsArr, choice, file)
    
    @app.route('/ai-choice/<name>')
    def getAiChoice(name):
        return ph.compChoice(name, file)
        

api.add_resource(PlayerRequests, '/<name>')

if __name__=='__main__':
    app.run(debug=True)