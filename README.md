# MELI-morse
Challenge Backend Mercado Libre

# main.py
Convierte un string en morse a texto humano.
Converte binario a código morse.
No es necesario instalar ninguna dependencia.

* Forma de uso:
Parametros para la ejeción

-t: tipo de lenguaje de input. Valores admitidos: [mor]: morse | [bin]: binario
-s: string a convertir. Valores admitidos: [0,1] en caso de seleccionar binario. | [A-Z a-z 0-9] en caso de seleccionar texto.
Ejemplo: python3 main.py -t bin -s "000110000011111001000"

Ejemplo: python3 main.py -t mor -s ".... --- .-.. .- -- . .-.. .."

# api.py
RECIBE REQUEST SIENDO UNA API RESTFUL
Convierte texto humano a codigo morse
Convierte código morse a humano.

Dependencias:

Flask: + 1.0.x
Flask-restful: + 0.3.7

#Forma de uso Online

* Transformar texto a morse

  * Mediante cURL: curl -X POST "http://35.230.95.39/translate/2morse" -d '{"text": "HOLA MELI"}'


* Transformar morse a texto (separar palabras por doble espacio)

  * Mediante cURL: curl -X POST "http://35.230.95.39/translate/2text" -d '{"text": ".... --- .-.. .- -- . .-.. .."}'
