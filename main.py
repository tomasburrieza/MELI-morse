# Autor: Tomas Burrieza
# Proyecto: Mercado Libre S.R.L - Backend Challenge "Morse"
# Fecha: Abril, 2019.


from Morse.Morse import *
import argparse
import sys

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-t", "--type", required=False,
                help="Especifica el tipo de input (bin: binario / mor: morse")

ap.add_argument("-s", "--string", required=False,
                help="String para realizar la conversión.")

args = vars(ap.parse_args())
type = args['type']
string = args['string']
MorseClass = Morse()


if type == "bin":
    assert MorseClass.isbin(string), "El texto ingresado no es binario puro."
    result = MorseClass.decodeBits2Morse(string)
elif type == "mor":
    assert MorseClass.ismor(string), "El texto ingresado no es morse puro."
    result = MorseClass.translate2Human(string)
else:
    assert False, "No se ha ingresado un metodo de conversion soportado. Utilice -t [bin] o [mor] "


print(result)
