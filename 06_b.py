import my_io

input = my_io.get_clipboard_contents()

initial_states = input.split(',')

fishes: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for initial_state in initial_states:
    fishes[int(initial_state)] += 1

for i in range(0, 256):

    to_add = 0

    for j in range(0, 9):
        if j == 0:
            to_add += fishes[j]
        else:
            fishes[j - 1] = fishes[j]

    fishes[6] += to_add
    fishes[8] = to_add

sum = 0

for i in range(0, 9):
    sum += fishes[i]

print(sum)
