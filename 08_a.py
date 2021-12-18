import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

sum = 0

for line in lines:

    vals = line.split(' ')

    i = vals[0:10]
    o = vals[-4:]

    for v in o:
        l = len(v)
        # 1 4 7 8
        if l == 2 or l == 4 or l == 3 or l == 7:
            sum += 1

print(sum)
