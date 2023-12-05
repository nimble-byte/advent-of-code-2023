from os import path
import re


class RangeMap:
    def __init__(self):
        self.mapping = []

    def __getitem__(self, key):
        # print(f"getting {key}")
        idx = 0
        for idx in range(len(self.mapping)):
            # print(f"  checking {self.mapping[idx]}")
            if self.mapping[idx]["end"] >= key >= self.mapping[idx]["start"]:
                # print(f"  returning {self.mapping[idx]["offset"] + key}")
                return self.mapping[idx]["offset"] + key
        return key

    def append(self, source, destination, steps):
        # print(f"  appending {source}, {destination}, {steps}")
        # print(f"  start {source}, end {source + steps - 1}, offset {destination - source}")
        item = {"start": source, "end": source + steps - 1, "offset": destination - source}
        self.mapping.append(item)
        self.mapping.sort(key=lambda x: x["start"])


def parse_map_input(chunk):
    lines = chunk.splitlines()

    mapping = RangeMap()

    for line in lines[1:]:
        destination_start, source_start, steps = re.findall(r"\d+", line)
        mapping.append(int(source_start), int(destination_start), int(steps))

    return mapping

input_chunks = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    input_chunks = f.read().split("\n\n")

seeds = [int(seed) for seed in re.findall(r"\d+", input_chunks[0])]

seed_to_soil = parse_map_input(input_chunks[1])
soil_to_fertilizer = parse_map_input(input_chunks[2])
fertilizer_to_water = parse_map_input(input_chunks[3])
water_to_light = parse_map_input(input_chunks[4])
light_to_temperature = parse_map_input(input_chunks[5])
temperature_to_humidity = parse_map_input(input_chunks[6])
humidity_to_location = parse_map_input(input_chunks[7])

def seed_to_location(seed):
    soil = seed_to_soil[seed]
    fertilizer = soil_to_fertilizer[soil]
    water = fertilizer_to_water[fertilizer]
    light = water_to_light[water]
    temperature = light_to_temperature[light]
    humidity = temperature_to_humidity[temperature]
    location = humidity_to_location[humidity]
    return location

result = [seed_to_location(seed) for seed in seeds]

print(f"The result for part 1 is {min(result)}")
