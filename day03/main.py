from os import path

GRID_SIZE = 140
PART_MARKERS = ["#", "$", "%", "&", "*", "+", "-", "/", "=", "@"]

# Read input (having the input available as grid helps this time around, but since strings can be accessed like arrays it should be fine)
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
        surroundings.append(list(grid[l][start_col:end_col]))

    return surroundings


sum_part_1 = 0
sum_part_2 = 0

part_candidates = []
gear_markers = []


for line in range(GRID_SIZE):
    col = 0

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

            part_value = int(input_grid[line][start : end + 1])
            surroundings = get_surroudings(input_grid, line, start, end)
            part_candidates.append((line, start, end, surroundings, part_value))

            col += 1
        elif input_grid[line][col] == "*":
            gear_markers.append((line, col))
            col += 1
        else:
            col += 1

for candidate in part_candidates:
    for line in candidate[3]:
        if any([s in PART_MARKERS for s in line]):
            sum_part_1 += candidate[4]
            break

for marker in gear_markers:
    print(f"Checking gear marker at {marker[0]}:{marker[1]}")
    parts = []

    for candidate in part_candidates:
        adjusted_line = marker[0] - candidate[0] + 1
        adjusted_col = marker[1] - candidate[1] + 1
        if adjusted_line >= 0 and adjusted_line < len(candidate[3]) and adjusted_col >= 0 and adjusted_col < len(candidate[3][adjusted_line]):
            # for line in candidate[3]:
            #     print(f"    {line}")
            if candidate[3][adjusted_line][adjusted_col] == "*":
                print("  MATCH")
                parts.append(candidate[4])
        else:
            continue
    if len(parts) == 2:
        sum_part_2 += parts[0] * parts[1]


print(f"The sum for part 1 is {sum_part_1}")
print(f"The sum for part 2 is {sum_part_2}") # 75805607
