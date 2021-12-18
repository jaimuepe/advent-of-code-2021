import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

delim = dict()
delim['('] = ')'
delim['['] = ']'
delim['{'] = '}'
delim['<'] = '>'

scoring = dict()
scoring[')'] = 3
scoring[']'] = 57
scoring['}'] = 1197
scoring['>'] = 25137


score = 0

for line in lines:
    
    opened_tokens = []
    
    for c in line:
        if c in delim:
            # opening token
            opened_tokens.append(c)
        else:
            # closing token
            last_token = opened_tokens.pop()
            if not delim[last_token] == c:
                # illegal line!
                score += scoring[c]
                break

print(score)