import plugboards
import rotors

from utils import letter_map


def init(reflector_name: str, rotor1_name: str, rotor2_name: str, rotor3_name: str):
    rotor_group = rotors.Rotors(
        reflector=rotors.Rotor(reflector_name),
        rotor1=rotors.Rotor(rotor1_name),
        rotor2=rotors.Rotor(rotor2_name),
        rotor3=rotors.Rotor(rotor3_name)
    )
    plugboard = plugboards.Plugboard()
    plugboard.scramble()

    return(rotor_group, plugboard)


def encrypt(enigma):

    while True:
        i = input("Type something? ")
        i = i.replace(" ", "")
        i = i.lower()

        plugboard_output = enigma[1].convert(i)
        rotors_output = enigma[0].convert(plugboard_output)
        plugboard_output = enigma[1].convert(rotors_output)

        print(f"\n#####\ninput:{i}\noutput:{plugboard_output}\n#####\n")


if __name__ == "__main__":
    enigma = init()
    encrypt(enigma)
