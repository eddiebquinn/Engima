import random
import json


class Plugboard():

    def __init__(self, plugboard_name: str = "default"):
        self.map = self.get_map(plugboard_name)

    def get_map(self, plugboard_name: str):
        json_file_path = f"resources/plugboard_maps/{plugboard_name}.json"
        with open(json_file_path, "r") as j:
            map_ = json.loads(j.read())
        return map_

    def scramble(self, scramble_level=10):
        if scramble_level > 13:
            print("You can only select a scramble level between 0 and 13")
        keys = list(self.map.keys())
        random.shuffle(keys)

        count = 0
        new_map = {}
        for key in keys:
            new_value = None
            if key in new_map.keys():
                continue
            if count >= scramble_level:
                new_value = self.map[key]
            else:
                new_value = random.choice(keys)
                while new_value == key or new_value in new_map.keys() or new_value == None:
                    new_value = random.choice(keys)

            new_map[key], new_map[new_value] = self.map[new_value], self.map[key]
            count = count + 1

        self.map = new_map

    def save_config(self, name: str):
        with open(f"resources/plugboard_maps/{name}.json", "w") as outfile:
            json.dump(self.map, outfile)

    def convert(self, input_: str):

        output = ""
        for item in input_:
            i = self.map[item]
            output = output + i
        return output
