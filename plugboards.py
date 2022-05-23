import random
import json


class Plugboard():

    def __init__(self, plugboard_name: str = "default"):
        self.map = self.get_map(plugboard_name)

    def get_map(self, plugboard_name: str):
        json_file_path = f"plugboard_maps/{plugboard_name}.json"
        with open(json_file_path, "r") as j:
            map_ = json.loads(j.read())
        return map_

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

    def save_config(self, name: str):
        with open(f"plugboard_maps/{name}.json", "w") as outfile:
            json.dump(self.map, outfile)

    def convert(self, input_: str):

        output = ""
        for item in input_:
            i = self.map[item]
            output = output + i
        return output
