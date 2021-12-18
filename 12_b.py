import my_io


def navigate(cave, path, connections, small_caves, repeated_small_cave, visited_small_caves):

    paths = []

    neighbors = connections[cave]

    for neighbor in neighbors:

        if neighbor == 'start':
            continue

        _repeated_small_cave = repeated_small_cave

        if neighbor.islower() and neighbor in visited_small_caves:
            if _repeated_small_cave:
                continue
            _repeated_small_cave = True

        _visited_small_caves = visited_small_caves.copy()
        _path = path.copy()

        if neighbor.islower():
            _visited_small_caves.add(neighbor)

        _path.append(neighbor)

        if neighbor == 'end':
            paths.append(_path)
        else:
            paths.extend(navigate(neighbor, _path,
                         connections, small_caves, _repeated_small_cave, _visited_small_caves))

    return paths


input = my_io.get_clipboard_contents()

lines = input.splitlines()

connections = dict()

small_caves = set()

for line in lines:

    (a, b) = line.split('-')

    if not a in connections:
        connections[a] = set()
    connections[a].add(b)

    if not b in connections:
        connections[b] = set()
    connections[b].add(a)

    if a != 'start' and a.islower():
        small_caves.add(a)
    if b != 'end' and b.islower():
        small_caves.add(b)

paths = navigate('start', ['start'], connections, small_caves, False, set())

print(len(paths))
