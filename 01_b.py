
import my_io

input = my_io.get_clipboard_contents()

previous_measurement = -1

first_measurement = True

count = 0

lines = input.splitlines()

line_count = len(lines)

for i in range(0, line_count - 2):

    measurement = 0
    measurement += int(lines[i])
    measurement += int(lines[i + 1])
    measurement += int(lines[i + 2])

    if not first_measurement:
        if measurement > previous_measurement:
            count = count + 1

    first_measurement = False

    previous_measurement = measurement

print(count)
