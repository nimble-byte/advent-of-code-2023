from operator import invert
from os import path
import sys
import re

# this likely won't work brute force like part 1, so I need a bit of a different approach


def parse_seed_ranges(chunk):
    seeds = []

    for start, steps in re.findall(r"(\d+) (\d+)", chunk):
        seeds.append((int(start), int(start) + int(steps) - 1))
    return seeds


def build_map(chunk):
    ranges = chunk.splitlines()[1:]
    mapping = []

    for range in ranges:
        destination, source, steps = map(int, re.findall(r"\d+", range))
        mapping.append((destination, source, steps))

    return mapping


def map_lookup(map, value):
    for dest, src, steps in map:
        if src <= value < src + steps:
            return dest + (value - src)
    return value


def inverse_lookup(cur_map, value):
    # print(cur_map)
    for dest, src, steps in cur_map:
        # print(f"  checking {dest}, {src}, {steps}")
        # it's really important that the second codition is < instead of <=; otherwise ranges overlap, breaking everything
        if dest <= value < dest + steps:
            return src + (value - dest)
    return value


def invert_map(cur_map, endpoints):
    map_endpoints = [
        [(dest, src), (dest + steps - 1, src + steps - 1)]
        for dest, src, steps in cur_map
    ]
    # flatten the list
    map_endpoints = [item for sublist in map_endpoints for item in sublist]
    # this is a little shady, but it works; maybe fix that up later
    map_endpoints.sort()

    # print("")
    # print(f"map: {cur_map}")
    # print(f"endpoints: {endpoints}")
    # print(f"map_endpoints: {map_endpoints}")

    out_endpoints = [inverse_lookup(cur_map, endpoint) for endpoint in endpoints]
    out_endpoints.sort()
    in_endpoints = set([input for (output, input) in map_endpoints])
    in_endpoints = sorted(in_endpoints)
    inverted_endpoints = set(out_endpoints).union(in_endpoints)
    inverted_endpoints = sorted(inverted_endpoints)

    # print(f"out_endpoints: {out_endpoints}")
    # print(f"in_endpoints: {in_endpoints}")
    # print("")

    return inverted_endpoints


def is_in_range(ranges, value):
    for start, end in ranges:
        if start <= value <= end:
            return True
    return False


input_chunks = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    input_chunks = f.read().split("\n\n")

seed_ranges = parse_seed_ranges(input_chunks[0])
# this is a little shady, but it works; maybe fix that up later
seed_ranges.sort()

seed_to_soil = build_map(input_chunks[1])
soil_to_fertilizer = build_map(input_chunks[2])
fertilizer_to_water = build_map(input_chunks[3])
water_to_light = build_map(input_chunks[4])
light_to_temperature = build_map(input_chunks[5])
temperature_to_humidity = build_map(input_chunks[6])
humidity_to_location = build_map(input_chunks[7])


def seed_to_location(seed):
    soil = map_lookup(seed_to_soil, seed)
    fertilizer = map_lookup(soil_to_fertilizer, soil)
    water = map_lookup(fertilizer_to_water, fertilizer)
    light = map_lookup(water_to_light, water)
    temperature = map_lookup(light_to_temperature, light)
    humidity = map_lookup(temperature_to_humidity, temperature)
    location = map_lookup(humidity_to_location, humidity)
    return location


humidity_endpoints = invert_map(humidity_to_location, [0, sys.maxsize])
temperature_endpoints = invert_map(temperature_to_humidity, humidity_endpoints)
light_endpoints = invert_map(light_to_temperature, temperature_endpoints)
water_endpoints = invert_map(water_to_light, light_endpoints)
fertilizer_endpoints = invert_map(fertilizer_to_water, water_endpoints)
soil_endpoints = invert_map(soil_to_fertilizer, fertilizer_endpoints)
seed_endpoints = invert_map(seed_to_soil, soil_endpoints)

filtered_seed_endpoints = [
    seed for seed in seed_endpoints if is_in_range(seed_ranges, seed)
]

locations = [seed_to_location(seed) for seed in filtered_seed_endpoints]
result = min(locations)

print(f"The result for part 2 is {result}")
