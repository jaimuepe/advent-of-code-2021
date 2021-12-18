import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

delim = dict()
delim['('] = ')'
delim['['] = ']'
delim['{'] = '}'
delim['<'] = '>'

scoring = dict()
scoring[')'] = 1
scoring[']'] = 2
scoring['}'] = 3
scoring['>'] = 4

scores = []

for line in lines:

    score = 0
    opened_tokens = []

    corrupted = False

    for c in line:
        if c in delim:
            # opening token
            opened_tokens.append(c)
        else:
            # closing token
            last_token = opened_tokens.pop()
            if not delim[last_token] == c:
                # corrupted line!
                corrupted = True
                break

    if not corrupted:

        for token in reversed(opened_tokens):
            closing_token = delim[token]
            score *= 5
            score += scoring[closing_token]

        scores.append(score)

scores.sort()

mid_score = scores[len(scores) // 2]

print(mid_score)
