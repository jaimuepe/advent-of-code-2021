
import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

template = lines[0]

rules = dict()

for i in range(2, len(lines)):
    (key, value) = lines[i].split(' -> ')
    rules[key] = value

steps = 10

for step in range(0, steps):

    next_index = 0

    while next_index < len(template) - 1:

        pair = template[next_index:next_index + 2]

        if pair in rules:
            template = template[:next_index + 1] + \
                rules[pair] + template[next_index + 1:]
            next_index += len(rules[pair]) + 1
        else:
            next_index += 1

    # print(template)

hits = dict()

for c in template:
    if c in hits:
        hits[c] += 1
    else:
        hits[c] = 1

most_common = 0
least_common = 10000000000

for c in template:
    if hits[c] > most_common:
        most_common = hits[c]
    elif hits[c] < least_common:
        least_common = hits[c]

print(most_common - least_common)
