
import my_io
import math


class Point:
    x1: int
    y1: int
    x2: int
    y2: int


def print_map(columns, board):

    for i in range(0, len(board)):

        if i > 0 and i % columns == 0:
            print()

        val = board[i] if board[i] > 0 else '.'
        print(val, end='')

    print()


input = my_io.get_clipboard_contents()

lines = input.splitlines()

x_max = -1
y_max = -1

points: list[Point] = []

for line in lines:

    (p1, _, p2) = line.split(' ')

    (x1, y1) = [int(a) for a in p1.split(',')]
    (x2, y2) = [int(a) for a in p2.split(',')]

    x_max = max(x_max, x1, x2)
    y_max = max(y_max, y1, y2)

    p = Point()
    p.x1 = x1
    p.y1 = y1
    p.x2 = x2
    p.y2 = y2

    points.append(p)

map = []

rows = x_max + 1
cols = y_max + 1

for i in range(0, rows * cols):
    map.append(0)

dangerous_coords_indices = []

dangerous_coords_count = 0

for point in points:

    (x1, y1, x2, y2) = (point.x1, point.y1, point.x2, point.y2)

    if x1 == x2:
        # h line

        start = y1 if y2 > y1 else y2
        end = y2 if y2 > y1 else y1

        for i in range(start, end + 1):

            map_index = x1 + i * rows
            map[map_index] += 1

            if map[map_index] > 1:
                if map_index not in dangerous_coords_indices:
                    dangerous_coords_indices.append(map_index)
                    dangerous_coords_count += 1

    elif y1 == y2:

        # v line

        start = x1 if x2 > x1 else x2
        end = x2 if x2 > x1 else x1

        for i in range(start, end + 1):

            map_index = i + y1 * rows
            map[map_index] += 1

            if map[map_index] > 1:
                if map_index not in dangerous_coords_indices:
                    dangerous_coords_indices.append(map_index)
                    dangerous_coords_count += 1

    else:
        # diagonal

        dx = int(math.copysign(1, x2 - x1))
        dy = int(math.copysign(1, y2 - y1))

        nx = abs(x2 - x1)

        for i in range(0, nx + 1):

            x = x1 + dx * i
            y = y1 + dy * i

            map_index = x + y * rows
            map[map_index] += 1

            if map[map_index] > 1:
                if map_index not in dangerous_coords_indices:
                    dangerous_coords_indices.append(map_index)
                    dangerous_coords_count += 1


print_map(cols, map)
print(dangerous_coords_count)
