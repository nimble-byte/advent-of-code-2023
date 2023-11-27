from os import path
import re

# Read input (having the input available as grid helps this time around, but since strings can be accessed like arrays it should be fine)

GRID_SIZE = 140


input_grid = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    input_grid = f.read().splitlines()


def get_surroudings(grid, line, start, end):
    # print(f"  Getting surroundings for {line}:{start}-{end}")
    surroundings = []
    start_line = max(0, line - 1)
    end_line = min(GRID_SIZE, line + 2)
    start_col = max(0, start - 1)
    end_col = min(GRID_SIZE, end + 2)

    # print(f"  Start line: {start_line}, end line: {end_line}")
    # print(f"  Start col: {start_col}, end col: {end_col}")

    for l in range(start_line, end_line):

        for c in range(start_col, end_col):
            if l == line and c >= start and c <= end:
                continue
            else:
                # print(f"    line: {l}, col: {c} - appending {grid[l][c]}")
                surroundings.append(grid[l][c])

    return surroundings


# Part 1
sum_part_1 = 0
sum_part_2 = 0

for line in range(GRID_SIZE):
    col = 0
    part_candidates = []

    while col < GRID_SIZE:
        if input_grid[line][col].isdigit():
            start = col
            end = col

            match_complete = False
            col += 1

            while not match_complete and col < GRID_SIZE:
                # print(f"  Checking {line}:{col} - {input_grid[line][col]}")
                if input_grid[line][col].isdigit():
                    if col == GRID_SIZE - 1:
                        end = col
                        match_complete = True
                    col += 1
                else:
                    end = col - 1
                    match_complete = True

            surroundings = get_surroudings(input_grid, line, start, end)
            part_value = int(input_grid[line][start : end + 1])
            # print(
            #     f"Found part value: {part_value} at {line}:{start}-{end} with surroundings of length {len(surroundings)}: {surroundings}"
            # )

            # assume anything that is not a digit is or a '.' is a part markerz`
            if any([s != "." for s in surroundings]):
                sum_part_1 += int(input_grid[line][start : end + 1])
            # print(f"  {surroundings}")
            col += 1

        else:
            col += 1

print(f"The sum for part 1 is {sum_part_1}")
print(f"The sum for part 2 is {sum_part_2}")
