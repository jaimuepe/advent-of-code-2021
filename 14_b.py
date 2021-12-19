
import my_io
import io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

template = lines[0]

rules = dict()

for i in range(2, len(lines)):
    (key, value) = lines[i].split(' -> ')
    rules[key] = value

replacements = dict()

for key in rules:

    replacement = rules[key]

    seq = key

    reps = 16 * [None]

    reps[0] = seq

    for i in range(1, 16):

        next_index = 0

        while next_index < len(seq) - 1:

            pair = seq[next_index:next_index + 2]
            replacement = rules[pair]

            if pair in rules:
                seq = seq[:next_index + 1] + \
                    replacement + seq[next_index + 1:]
                next_index += 2
            else:
                next_index += 1

        reps[i] = seq

    replacements[key] = reps

chain = template

for i in [15, 15, 10]:

    buff = io.StringIO()

    for j in range(0, len(chain) - 1, 1):

        pair = chain[j:j+2]
        rep = replacements[pair][i]

        buff.write(rep[:len(rep)-1])

    buff.write(rep[-1:])
    chain = buff.getvalue()

    # print(len(chain))

hits = dict()

for c in chain:
    if c in hits:
        hits[c] += 1
    else:
        hits[c] = 1

most_common = float('-inf')
least_common = float('inf')

for c in hits:
    if hits[c] > most_common:
        most_common = hits[c]
    elif hits[c] < least_common:
        least_common = hits[c]

print(most_common - least_common)
