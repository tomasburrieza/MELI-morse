# Autor: Tomas Burrieza
# Proyecto: Mercado Libre S.R.L - Backend Challenge "Morse"
# Fecha: Abril, 2019.


from Morse.Morse import *

# modificar las variables para obtener diferentes resultados.

test = "111110011111100000111000000100111110010011000011001100"
test_morse = "-- . .-.. .."


MorseClass = Morse()



print("\n\nBienvenido/a al conversor de Morse-Binario-Texto. \n\nTransformando {} a binario...".format(test))


morse_code = MorseClass.decodeBits2Morse(test)

print("RESULTADO:  {}".format(morse_code))

print("\nTransformando MORSE:  {}  a texto... \n".format(test_morse))

print("RESULTADO:  {}".format(MorseClass.translate2Human(morse_code)))

print("\n\n")

print("Gracias por utilizar el conversor :)")



