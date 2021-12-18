
import my_io
import io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

template = lines[0]

rules = dict()

for i in range(2, len(lines)):
    (key, value) = lines[i].split(' -> ')
    rules[key] = value

steps = 40

hits = dict()

for c in template:    
    if c in hits:
        hits[c] += 1
    else:
        hits[c] = 1

buff = list(template)

for step in range(0, steps):

    next_index = 0

    pairs = []

    for i in range(0, len(template), 2):
        pairs.append(template[i:i+2])

    for pair in pairs:
        insert = rules[pair]

    # todo find a better algorithm, this one is slow
    
    # while next_index < len(buff) - 1:

    #     pair = str(buff[next_index:next_index + 2])

    #     if pair in rules:

    #         insert = rules[pair]

    #         buff.insert(next_index, insert)

    #         next_index += 2

    #         if insert in hits:
    #             hits[insert] += 1
    #         else:
    #             hits[insert] = 1

    #     else:
    #         next_index += 1

most_common = 0
least_common = 10000000000

for c in template:
    if hits[c] > most_common:
        most_common = hits[c]
    elif hits[c] < least_common:
        least_common = hits[c]

print(most_common - least_common)
