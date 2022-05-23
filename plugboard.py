import random


class Plugboard():

    def __init__(self):
        self.map = {
            "a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g",
            "h": "h", "i": "i", "j": "j", "k": "k", "l": "l", "m": "m", "n": "n",
            "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "u",
            "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"
        }

    def scramble(self):
        keys = list(self.map.keys())

        new_map = {}
        for key in keys:
            if key in new_map.keys():
                continue
            new_val = random.choice(keys)
            while new_val == key or new_val in new_map.keys():
                new_val = random.choice(keys)

            new_map[key] = new_val
            new_map[new_val] = key

        self.map = new_map

    def convert(self, input_: str):

        output = []
        for item in input_:
            i = self.map[item]
            output.append(i)
        return output
