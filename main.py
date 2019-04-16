# Autor: Tomas Burrieza
# Proyecto: Mercado Libre S.R.L - Backend Challenge "Morse"
# Fecha: Abril, 2019.


from Morse.Morse import *
import argparse
import sys


if  __name__ == '__main__':
    arg = argparse.ArgumentParser()

    arg.add_argument("-t", "--type", required=False,
                    help="Especifica el tipo de input (bin: binario / mor: morse")

    arg.add_argument("-s", "--string", required=False,
                    help="String para realizar la conversión.")

    args = vars(arg.parse_args())
    type = args['type']
    string = args['string']
    MorseClass = Morse()

    if type == "bin":
        result = MorseClass.decodeBits2Morse(string)
    elif type == "mor":
        result = MorseClass.translate2Human(string)
    else:
        assert False, "No se ha ingresado un metodo de conversion soportado. Utilice -t [bin] o [mor]. Ejemplo: python3 main.py -t mor -s '. .. ...'"

    print(result)