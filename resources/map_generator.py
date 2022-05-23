import json
import pprint


def generate(input_: str, notch: list):
    """Generates a rotor map based on a 26 letter string of unique characters

    Args:
        input_ (str): 26 letter string of unique characters
        notch (list): Positions of notches on the rotor

    Returns:
        _type_: _description_
    """
    input_ = list(input_)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    r_map = {}
    for letter in input_:
        position = input_.index(letter)
        r_map[alphabet[position]] = letter.lower()

    rotor_map = {
        "notch": notch,
        "map": r_map
    }
    return rotor_map


def write_to_file(rotor_name: str, input_: str, notch: list = None):
    """Uses the generate function and prints output to file

    Args:
        rotor_name (str): The historic name of the rotor in question
        input_ (str): 26 letter string of unique characters
        notch (list, optional): Positions of notches on the rotor. Defaults to None.
    """
    rotor_map = generate(input_, notch)
    with open(f"rotor_maps/{rotor_name}.json", "w") as outfile:
        json.dump(rotor_map, outfile)


write_to_file("1924-IC", "DMTWSILRUYQNKFEJCAZBPGXOHV")
write_to_file("1924-IIC", "HQZGPJTMOBLNCIFDYAWVEUSRKX")
write_to_file("1924-IIC", "UQNTLSZFMREHDPXKIBVYGJCWOA")

write_to_file("1941-I", "JGDQOXUSCAMIFRVTPNEWKBLZYH")
write_to_file("1941-II", "NTZPSFBOKMWRCJDIVLAEYUXHGQ")
write_to_file("1941-III", "JVIUBHTCDYAKEQZPOSGXNRMWFL")
write_to_file("1941-UKW", "QYHOGNECVPUZTFDJAXWMKISRBL")
write_to_file("1941-ETW", "QWERTZUIOASDFGHJKPYXCVBNML")

write_to_file("1939-I-K", "PEZUOHXSCVFMTBGLRINQJWAYDK")
write_to_file("1939-II-K	", "ZOUESYDKFWPCIQXHMVBLGNJRAT")
write_to_file("1939-III-K", "EHRVXGAOBQUSIMZFLYNWKTPDJC")
write_to_file("1939-UKW-K", "IMETCGFRAYSQBZXWLHKDVUPOJN")
write_to_file("1939-ETW-K", "QWERTZUIOASDFGHJKPYXCVBNML")

write_to_file("1930-I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", ["Q"])
write_to_file("1930-II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", ["E"])
write_to_file("1930-III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", ["V"])
write_to_file("1938-IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", ["J"])
write_to_file("1938-V", "VZBRGITYUPSDNHLXAWMJQOFECK", ["Z"])
write_to_file("1939-VI", "JPGVOUMFYQBENHZRDKASXLICTW", ["Z", "M"])
write_to_file("1939-VII", "NZJHGRCXMYSWBOUFAIVLPEKQDT", ["Z", "M"])
write_to_file("1939-VIII", "FKQHTLXOCBJSPDZRAMEWNIUYGV", ["Z", "M"])

write_to_file("1941-Beta", "LEYJVCNIXWPBQMDRTAKZGFUHOS")
write_to_file("1942-Gamma", "FSOKANUERHMBTIYCWLQPZXVGJD")
write_to_file("NA-ReflectorA", "EJMZALYXVBWFCRQUONTSPIKHGD")
write_to_file("NA-ReflectorB", "YRUHQSLDPXNGOKMIEBFZCWVJAT")
write_to_file("NA-ReflectorC", "FVPJIAOYEDRZXWGCTKUQSBNMHL")
write_to_file("1940-ReflectorBt", "ENKQAUYWJICOPBLMDXZVFTHRGS")
write_to_file("1940-ReflectorCt", "RDOBJNTKVEHMLFCWZAXGYIPSUQ")
write_to_file("NA-ETW", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
