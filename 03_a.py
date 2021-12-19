
import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

n_lines = len(lines)
n_digits = len(lines[0])

gamma_rate = 0
epsilon_rate = 0

for i in range(0, n_digits):

    sum = 0

    for line in lines:
        if line[i] == '1':
            sum += 1

    if sum > n_lines / 2:
        # gamma
        gamma_rate += pow(2, n_digits - 1 - i)
        pass
    else:
        # epsilon
        epsilon_rate += pow(2, n_digits - 1 - i)
        pass

print(f'gamma = {gamma_rate}')
print(f'epsilon = {epsilon_rate}')

print(gamma_rate * epsilon_rate)
