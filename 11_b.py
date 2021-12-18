import my_io


def print_grid(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            print(grid[i][j], end='')
        print()
    print()


def flash(x, y, grid):

    flashed_octopuses = []

    for i in range(y - 1, y + 2):

        if i < 0 or i > len(grid) - 1:
            continue

        for j in range(x - 1, x + 2):

            if j < 0 or j > len(grid[0]) - 1:
                continue

            if i == y and j == x:
                # continue
                pass
            
            if (grid[i][j] == 50):
                continue

            grid[i][j] += 1

            if grid[i][j] == 10:
                grid[i][j] = 50
                flashed_octopuses.append((j, i))
                flashed_octopuses.extend(flash(j, i, grid))

    return flashed_octopuses


input = my_io.get_clipboard_contents()

lines = input.splitlines()

grid = []


for line in lines:
    grid.append([int(x) for x in line])

h = len(grid)
w = len(grid[0])

step = 0

while True:

    # print_grid(grid)

    flashed_octopuses = []

    for x in range(0, w):
        for y in range(0, h):

            if grid[y][x] == 50:
                continue

            grid[y][x] += 1

            if grid[y][x] == 10:
                grid[y][x] = 50
                flashed_octopuses.append((x, y))
                flashed_octopuses.extend(flash(x, y, grid))

    for (x, y) in flashed_octopuses:
        grid[y][x] = 0

    if len(flashed_octopuses) == w * h:
        break

    step += 1

print(step + 1)
