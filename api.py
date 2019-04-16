# Autor: Tomas Burrieza
# Proyecto: Mercado Libre S.R.L - Backend Challenge "Morse" API
# Fecha: Abril, 2019.


from Morse.Morse import *
from flask import request, Flask
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)


class Morse2Text(Resource):
    def post(self):
        json = request.get_json(force=True)
        morse_string = json['text']
        print(morse_string)

        morse = Morse()
        result = {'response': morse.translate2Human(morse_string), "code": 200}
        return result,200


class Text2Morse(Resource):
    def post(self):

        json = request.get_json(force=True)
        print(json)
        text_string = json['text']
        print(text_string)

        print(request)
        print(text_string)

        morse = Morse()
        result = {'response': morse.human2morse(text_string.upper()), "code": 200}
        return result, 200


api.add_resource(Morse2Text, '/translate/2text')
api.add_resource(Text2Morse, '/translate/2morse')

if __name__ == '__main__':
    application.run(port='8840', debug=True)
