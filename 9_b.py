import my_io
import math

input = my_io.get_clipboard_contents()

lines = input.splitlines()

grid = []

h = len(lines)
w = len(lines[0])


def get_basin(x, y) -> list[(int, int)]:

    neighbors = []
    neighbors.append((x, y))

    num = grid[y][x]

    for yy in range(y - 1, y + 2):

        if yy < 0 or yy > h - 1 or yy == y:
            continue

        neighbor = grid[yy][x]

        if neighbor != 9 and neighbor > num:
            neighbors.extend(get_basin(x, yy))

    for xx in range(x - 1, x + 2):

        if xx < 0 or xx > w - 1 or xx == x:
            continue

        neighbor = grid[y][xx]

        if neighbor != 9 and neighbor > num:
            neighbors.extend(get_basin(xx, y))

    return neighbors


for line in lines:
    row = []
    for num in line:
        row.append(int(num))
    grid.append(row)

low_points = []

for y in range(0, h):

    for x in range(0, w):

        num = grid[y][x]

        neighbors = []

        if x > 0:
            neighbors.append(grid[y][x - 1])

        if x < w - 1:
            neighbors.append(grid[y][x + 1])

        if y > 0:
            neighbors.append(grid[y - 1][x])

        if y < h - 1:
            neighbors.append(grid[y + 1][x])

        lowest = True

        for neighbor in neighbors:
            if neighbor <= num:
                lowest = False

        if lowest:
            low_points.append((x, y))

# risk_level = sum(x + 1 for x in low_points)

basins = []

for low_point in low_points:

    basin = set(get_basin(low_point[0], low_point[1]))
    basins.append(len(basin))

basins.sort(reverse=True)

result = math.prod(basins[:3])

print(result)