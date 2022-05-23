import json


class Rotor():

    def __init__(self, rotor_name: str = "default", ring_setting: int = 0):
        self.name = rotor_name
        self.offset = 0
        self.ring_setting = ring_setting

        self.map = self.get_map(self.name, self.ring_setting)

    def get_map(self, rotor_name: str, ring_setting: int):
        json_file_path = f"rotor_maps/{rotor_name}.json"
        with open(json_file_path, "r") as j:
            map_ = json.loads(j.read())

        if self.ring_setting != 0:
            map_["map"] = self.offset_map(map_["map"])

        return map_

    def offset_map(self, map_: dict):
        keys = list(map_.keys())
        old_vals = list(map_.values())
        new_map = {}
        for key in keys:
            index = keys.index(key)
            new_index = self.get_index(index)
            new_map[key] = old_vals[new_index]
        return new_map

    def get_index(self, index: int):
        max_val = (25 - self.ring_setting) + 1
        if index >= max_val:
            new_index = index - max_val
        else:
            new_index = index + self.ring_setting
        return new_index

    def click(self):
        self.offset = 0 if self.offset == 25 else self.offset + 1
        print(self.offset)
        print("click")

    def convert(self, _input: str, click: bool = False):
        output = ""
        for i in _input:
            output = output + self.map["map"][i]

        return output


class Rotors():

    def __init__(self, reflector, rotor1, rotor2, rotor3):
        self.reflor = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.rotors = [self.rotor1, self.rotor2, self.rotor3]

    def print_config(self):
        print(
            f"[{self.reflor.name} | {self.rotor3.name} | {self.rotor2.name} | {self.rotor1.name}]")

    def convert(self, input_: str):
        output_complete = ""
        for i in input_:
            output = ""
            for rotor in self.rotors:
                output = rotor.convert(i)
            output = self.reflor.convert(output)
            for rotor in self.rotors[::-1]:
                output = rotor.convert(output)
            output_complete = output_complete + output
        return output_complete
