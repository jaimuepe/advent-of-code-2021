
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

# generate replacements from 0-10 steps

for key in rules:

    replacement = rules[key]

    seq = key

    reps = 41 * [None]

    reps[0] = seq

    for i in range(1, 11):

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

# generate replacements for 20 steps



for key in rules:

    reps = replacements[key]

    seq = reps[10]

    buff = io.StringIO()

    for j in range(0, len(seq) - 1, 1):

        pair = seq[j:j+2]
        rep = replacements[pair][10]

        buff.write(rep[:len(rep)-1])

    buff.write(rep[-1:])

    reps[20] = buff.getvalue()

# iterate template and count

for j in range(0, len(template) - 1, 1):

    pair = template[j:j+2]
    rep = replacements[pair][i]

    buff.write(rep[:len(rep)-1])

buff.write(rep[-1:])
chain = buff.getvalue()

# generate replacements for 40 steps

for key in rules:

    reps = replacements[key]

    seq = reps[20]

    segments = [None] * (len(seq) + 1)

    for j in range(0, len(seq)):

        pair = seq[j:j+2]
        rep = replacements[pair][20]

        segments[j] = rep[:len(rep)-1]

    segments[j + 1] = rep[-1:]

    reps[40] = ''.join(segments)

chain = template

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
