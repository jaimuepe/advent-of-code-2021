
import my_io
import io

# ugliest code ever writter, probably

input = my_io.get_clipboard_contents()

uniques = set()

lines = input.splitlines()

template = lines[0]

for c in template:
    uniques.add(c)

rules = dict()

for i in range(2, len(lines)):

    (key, value) = lines[i].split(' -> ')
    rules[key] = value

    (k1, k2) = key
    uniques.add(k1)
    uniques.add(k2)
    uniques.add(value)

replacements = dict()

# generate replacements from 0-10 steps

for key in rules:

    replacement = rules[key]

    seq = key

    reps = 21 * [None]

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

    for j in range(0, len(seq) - 1):

        pair = seq[j:j+2]
        rep = replacements[pair][10]

        buff.write(rep[:len(rep)-1])

    buff.write(rep[-1:])

    reps[20] = buff.getvalue()

template20 = ''

for i in range(0, len(template) - 1):

    pair = template[i:i+2]
    rep = replacements[pair][20]

    template20 += rep[:len(rep) - 1]
template20 += rep[-1:]

hits = dict()

hits_dict = dict()

for key in rules:

    hits_dict[key] = dict()

    for k in uniques:
        hits_dict[key][k] = 0

    rep = replacements[key][20]

    for i in range(0, len(rep) - 1):

        c = rep[i]
        hits_dict[key][c] += 1

hits = dict()

for k in uniques:
    hits[k] = 0

for i in range(0, len(template20) - 1):

    pair = template20[i: i+2]
    hits20 = hits_dict[pair]

    for k in uniques:
        hits[k] += hits20[k]

hits[template20[len(template20) - 1]] += 1

print(hits)
