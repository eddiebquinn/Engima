import json


class Rotor():

    def __init__(self, rotor_name: str = "default", ring_setting: int = 0):
        self.offset = 0
        self.ring_setting = ring_setting
        self.map = self.get_map(rotor_name, self.ring_setting)
        print(self.map)

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
