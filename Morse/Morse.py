# Morse Package
# Contiene todas las funciones utiles para la transformación de información a Morse o viceversa.

#regEx
import re


class MorseAVG():
    def __init__(self):
        self.mincero = 0
        self.maxcero = 0
        self.minone = 0
        self.maxone = 0
        self.end = 0


class PulseType:
    shortCero = 0
    longCero = 1
    shortOne = 2
    longOne = 3
    end = 4


class Morse():
    def __init__(self):
        self.avg = MorseAVG()
        self.morse_dict = {
            ".-": "A",
            "-...": "B",
            "-.-.": "C",
            "-..": "D",
            ".": "E",
            "..-.": "F",
            "--.": "G",
            "....": "H",
            "..": "I",
            ".---": "J",
            "-.-": "K",
            ".-..": "L",
            "--": "M",
            "-.": "N",
            "---": "O",
            ".--.": "P",
            "--.-": "Q",
            ".-.": "R",
            "...": "S",
            "-": "T",
            "..-": "U",
            "...-": "V",
            ".--": "W",
            "-..-": "X",
            "-.--": "Y",
            "--..": "Z",
            "-----": "0",
            ".----": "1",
            "..---": "2",
            "...--": "3",
            "....-": "4",
            ".....": "5",
            "-....": "6",
            "--...": "7",
            "---..": "8",
            "----.": "9",
            ".-.-.-": ".",
            " ": " "  # espacio si hay más de una palabra siempre es espacio.
        }

        self.reverse_morse_dict = {morse: char for char, morse in self.morse_dict.items()}

    def translate2Human(self, morse):
        morse_pulses_master = morse.split("  ")
        human_text = ""

        for morse_pulses in morse_pulses_master:
            for pulse in morse_pulses.split(" "):
                char = self.morse_dict.get(pulse) or ""

                human_text += char

            human_text += " "

        return human_text

    def decodeBits2Morse(self, bits):
        decoded_bits = ""  # variable para almacenar los bits decodificados
        self.avg = self.getPulseAverage(bits)  # promedio para evaluar el tipo de pulso (corto o largo)
        pulses = (re.findall('(0+|1+)', bits))  # array de bits separados entre 0 y 1 por órden de aparición

        for p in pulses:
            eval = self.evaluate(p)
            if eval == PulseType.shortOne:
                decoded_bits += "."
            elif eval == PulseType.longOne:
                decoded_bits += "-"
            elif eval == PulseType.longCero:
                decoded_bits += " "
            elif eval == PulseType.shortCero:
                decoded_bits += ""
            elif eval == PulseType.end:
                decoded_bits += ""

        return decoded_bits

    def evaluate(self, pulse):
        pulse_type = pulse[0]
        if pulse_type == str(1):
            if len(pulse) < ((self.avg.maxone + self.avg.minone) / 2):
                return PulseType.shortOne
            else:
                return PulseType.longOne

        elif pulse_type == str(0):
            if len(pulse) < ((self.avg.maxcero + self.avg.mincero) / 2):
                return PulseType.shortCero
            elif len(pulse) == self.avg.end:
                return PulseType.end
            else:
                return PulseType.longCero

<<<<<<< HEAD
    def isbin(self, string):
        return set(string) <= set('01')

    def ismor(self, string):
        return set(string) <= set('.- ')

=======
>>>>>>> b400ab75cea8bc48f7ad594d61b35527dcff14c4
    def getPulseAverage(self, bits):
        ceropulses = (re.findall('(0+)', bits))

        onepulses = (re.findall('(1+)', bits))

        end = ceropulses[-1]

        del ceropulses[-1]  # no nos sirve contar la información final siempre que sean ceros.
        del ceropulses[0]  # tampoco la inicial :)

        mincero = min(ceropulses)
        maxcero = max(ceropulses)

        minone = min(onepulses)
        maxone = max(onepulses)

        ret_morse_avg = MorseAVG()

        ret_morse_avg.mincero = len(mincero)
        ret_morse_avg.maxcero = len(maxcero)
        ret_morse_avg.end = len(end)
        ret_morse_avg.minone = len(minone)
        ret_morse_avg.maxone = len(maxone)

        return ret_morse_avg

    def human2morse(self, text):
        palabras = text.split(" ")
        morse_text = ""

        for p in palabras:
            for i in range(len(p)):
                char = self.reverse_morse_dict.get(p[i]) or ""

                morse_text += char

                morse_text += " "

            morse_text += " "

        return morse_text
<<<<<<< HEAD


=======
>>>>>>> b400ab75cea8bc48f7ad594d61b35527dcff14c4
