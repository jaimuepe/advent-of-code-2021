import my_io


class LanternFish:

    timer: int = 0

    def Tick(self) -> bool:

        self.timer -= 1
        if self.timer == -1:
            self.timer = 6
            return True

        return False


def print_state(day: int, fishes: list[LanternFish]):

    header = 'Initial state: ' if day == -1 else f'After {day} day(s): '
    print(header, end=' ')

    for i in range(0, len(fishes)):
        print(fishes[i].timer, ',' if i < len(
            fishes) - 1 else '', sep='', end='')
    print()


input = my_io.get_clipboard_contents()

initial_states = input.split(',')

fishes: list[LanternFish] = []

for initial_state in initial_states:
    fish = LanternFish()
    fish.timer = int(initial_state)
    fishes.append(fish)

# print_state(-1, fishes)

for i in range(0, 256):

    n = 0
    for lanternFish in fishes:
        if lanternFish.Tick():
            n += 1

    for j in range(0, n):
        fish = LanternFish()
        fish.timer = 8
        fishes.append(fish)

    # print_state(i + 1, fishes)

print(len(fishes))
