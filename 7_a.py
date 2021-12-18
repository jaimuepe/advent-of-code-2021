import my_io

input = my_io.get_clipboard_contents()

vals = [int(x) for x in input.split(',')]

best_accumulated_distance = 100000000
best_position = 0

max_h = max(vals)

for i in range(0, max_h + 1):

    accumulated_distance = 0

    for val in vals:
        accumulated_distance += abs(val - i)

    if accumulated_distance < best_accumulated_distance:
        best_position = i
        best_accumulated_distance = accumulated_distance

print(best_position)
print(best_accumulated_distance)
