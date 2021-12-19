
import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

n_digits = len(lines[0])

gamma_rate = 0
epsilon_rate = 0


def filter_values(index, values, mcv):

    n_lines = len(values)

    if len(values) == 1:
        return values[0]

    sum = 0

    ones = []
    zeros = []

    for line in values:
        if line[index] == '1':
            ones.append(line)
            sum += 1
        else:
            zeros.append(line)

    if sum >= n_lines / 2:
        if mcv:
            return filter_values(index + 1, ones, mcv)
        else:
            return filter_values(index + 1, zeros, mcv)
    else:
        if mcv:
            return filter_values(index + 1, zeros, mcv)
        else:
            return filter_values(index + 1, ones, mcv)


def binary_to_decimal(num):
    return int(num, 2)


oxygen_generator_rating = filter_values(0, lines, True)
co2_scrubber_rating = filter_values(0, lines, False)

ogr = binary_to_decimal(oxygen_generator_rating)
csr = binary_to_decimal(co2_scrubber_rating)

print(ogr * csr)
