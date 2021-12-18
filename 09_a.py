import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

grid = []

h = len(lines)
w = len(lines[0])

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
            low_points.append(num)

risk_level = sum(x + 1 for x in low_points)

print(risk_level)
