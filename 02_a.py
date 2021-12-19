
import my_io

input = my_io.get_clipboard_contents()

h_pos = 0
v_pos = 0

lines = input.splitlines()

for line in lines:

    [direction, amount] = line.split()

    if direction == 'forward':
        h_pos += int(amount)
    elif direction == 'down':
        v_pos += int(amount)
    elif direction == 'up':
        v_pos -= int(amount)
    else:
        raise ValueError(f'direction {direction} not handled')

print(h_pos * v_pos)
