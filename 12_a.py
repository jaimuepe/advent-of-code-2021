import my_io


def navigate(cave, path, connections, small_caves, visited_small_caves):

    paths = []

    neighbors = connections[cave]

    for neighbor in neighbors:

        if neighbor == 'start':
            continue

        if neighbor.islower() and neighbor in visited_small_caves:
            continue

        visited_small_caves_copy = visited_small_caves.copy()
        path_copy = path.copy()

        if neighbor.islower():
            visited_small_caves_copy.add(neighbor)

        path_copy.append(neighbor)

        # print(path_copy)

        if neighbor == 'end':
            paths.append(path_copy)
        else:
            paths.extend(navigate(neighbor, path_copy,
                         connections, small_caves, visited_small_caves_copy))

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

paths = navigate('start', ['start'], connections, small_caves, set())

print(len(paths))
