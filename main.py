import objects.enigma as enigma_


def init(reflector_name, rotor1_name, rotor2_name, rotor3_name):
    enigma = enigma_.Enigma(
        reflector_name=reflector_name,
        rotor1_name=rotor1_name,
        rotor2_name=rotor2_name,
        rotor3_name=rotor3_name)
    return enigma


if __name__ == "__main__":
    enigma = init()
    enigma.encrypt()
