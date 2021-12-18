import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()


def print_grid(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            print(grid[i][j], end='')
        print()


grid = []

# read the coords

w = 0
h = 0

points = []

for i in range(0, len(lines)):

    line = lines[i]

    if line == '':
        break

    (x, y) = line.split(',')

    x = int(x)
    y = int(y)

    w = max(w, x + 1)
    h = max(h, y + 1)

    points.append((x, y))

if w % 2 == 0:
    w += 1

if h % 2 == 0:
    h += 1

instructions_index = i + 1

for i in range(0, h):
    grid.append(['.'] * w)

for (x, y) in points:
    grid[y][x] = '#'

for i in range(instructions_index, len(lines)):

    instruction_line = lines[i]
    idx = instruction_line.index('=')

    axis = instruction_line[idx - 1]
    value = int(instruction_line[idx + 1:])

    width = len(grid[0])
    height = len(grid)

    half_width = width // 2
    half_height = height // 2

    if axis == 'x':
        # fold horizontally
        for x in range(0, half_width):
            for j in range(0, height):
                lower_val = grid[j][width - x - 1]
                if lower_val == '#':
                    grid[j][x] = '#'

        for k in range (0, len(grid)):
            grid[k] = grid[k][0:half_width]

    else:
        # fold vertically
        for y in range(0, half_height):
            for j in range(0, width):
                lower_val = grid[height - y - 1][j]
                if lower_val == '#':
                    grid[y][j] = '#'

        grid = grid[:half_height]
        
    break

sum = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] == '#':
            sum += 1

print(sum)
