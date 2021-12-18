
import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

sequence = lines[0].split(',')

boards = []

# skip 2 first rows
i = 2

while i < len(lines):

    board = []

    for j in range(0, 5):

        line = lines[i].strip()
        vals = line.split()

        row = []

        for k in range(0, 5):
            row.append(vals[k])

        board.append(row)

        i += 1

    boards.append(board)

    i += 1

hits = []

for i in range(0, len(boards)):
    hits.append(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])

winner_boards = []
winning_numbers = []

for num in sequence:

    for i in range(0, len(boards)):
        
        if (i in winner_boards):
            continue

        board = boards[i]

        for j in range(0, 5):

            for k in range(0, 5):

                val = board[j][k]

                if val == num:

                    hits[i][j][k] = 1

                    r_count = 0
                    c_count = 0

                    for r in range(0, 5):
                        if hits[i][r][k] == 1:
                            c_count += 1
                        if hits[i][j][r] == 1:
                            r_count += 1

                    if r_count == 5 or c_count == 5:

                        winning_numbers.append(int(val))

                        if len(winner_boards) == len(boards) - 1:

                            sum = 0

                            for x in range(0, 5):
                                for y in range(0, 5):
                                    if hits[i][x][y] == 0:
                                        sum += int(board[x][y])

                            score = sum * int(val)
                            print(score)
                            quit()

                        else:
                            if (i not in winner_boards):
                                winner_boards.append(i)
