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
            content = json.loads(j.read())

        # Write code that offsets map based on ring setting, here

        return content

    def click(self):
        self.offset = 0 if self.offset == 25 else self.offset + 1
        print(self.offset)
        print("click")
