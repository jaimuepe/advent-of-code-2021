
import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()


def get_neighbors(x, y, grid) -> list[tuple[int, int]]:

    neighbors = []

    if x > 0:
        neighbors.append((x - 1, y))
    if x < len(grid[0]) - 1:
        neighbors.append((x + 1, y))

    if y > 0:
        neighbors.append((x, y - 1))
    if y < len(grid) - 1:
        neighbors.append((x, y + 1))

    return neighbors


grid = []

for line in lines:
    grid.append([int(x) for x in line])


class node_path:
    x: int
    y: int
    cost: int

    def __eq__(self, obj):
        return self.x == obj[0] and self.y == obj[1]


def traverse(
        node: node_path,
        grid: list[list],
        best_risk: int,
        visited_nodes: dict[tuple[int, int], node_path]) -> int:

    neighbors = get_neighbors(node.x, node.y, grid)

    for neighbor in neighbors:

        (x, y) = (neighbor[0], neighbor[1])

        risk = node.cost + grid[y][x]

        if risk >= best_risk:
            continue

        if (x, y) in visited_nodes:

            visited_risk = visited_nodes[(x, y)].cost

            if risk >= visited_risk:
                continue

        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            best_risk = risk
            continue

        visited_node = node_path()
        visited_node.x = x
        visited_node.y = y
        visited_node.cost = risk

        visited_nodes[(x, y)] = visited_node

        best_risk = traverse(visited_node, grid, best_risk, visited_nodes)

    return best_risk


start_node = node_path()
start_node.x = 0
start_node.y = 0
start_node.cost = 0

# lets get a starting path so we can find shorter ones

start_risk = 0

# don't count the first cell

for i in range(1, len(grid[0])):
    start_risk += grid[0][i]

for i in range(1, len(grid)):
    start_risk += grid[i][len(grid[0]) - 1]

best_risk = traverse(start_node, grid, start_risk, dict())

print(best_risk)
