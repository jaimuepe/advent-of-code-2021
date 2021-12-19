
import my_io

input = my_io.get_clipboard_contents()

previous_measurement = -1

first_measurement = True

count = 0

for line in input.splitlines():

    measurement = int(line.strip())

    if not first_measurement:
        if measurement > previous_measurement:
            count = count + 1

    first_measurement = False

    previous_measurement = measurement

print(count)
