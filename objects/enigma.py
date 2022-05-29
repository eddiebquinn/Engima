import objects.rotors as rotors
import objects.plugboards as plugboards


class Enigma():

    def __init__(self, reflector_name: str, rotor1_name: str, rotor2_name: str, rotor3_name: str):
        self.rotor_group = rotors.Rotors(
            reflector=rotors.Rotor(reflector_name),
            rotor1=rotors.Rotor(rotor1_name),
            rotor2=rotors.Rotor(rotor2_name),
            rotor3=rotors.Rotor(rotor3_name))

        self.plugboard = plugboards.Plugboard()
        self.plugboard.scramble()

    def encrypt(self):
        while True:
            i = input("Type something? ").lower().replace(" ", "")

            plugboard_output = self.plugboard.convert(i)
            rotors_output = self.rotor_group.convert(plugboard_output)
            plugboard_output = self.plugboard.convert(rotors_output)

            print(f"\n#####\ninput:{i}\noutput:{plugboard_output}\n#####\n")
