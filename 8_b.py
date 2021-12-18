import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()

sum = 0

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for line in lines:

    vals = line.split(' ')

    i = vals[0:10]
    o = vals[-4:]

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0

    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # determine where 1, 4, 7, 8 go
    for v in i:
        if len(v) == 2:
            nums[1] = v
        elif len(v) == 4:
            nums[4] = v
        elif len(v) == 3:
            nums[7] = v
        elif len(v) == 7:
            nums[8] = v

    ii = i.copy()

    ii.remove(nums[1])
    ii.remove(nums[4])
    ii.remove(nums[7])
    ii.remove(nums[8])

    # exclusive segment between 7 and 8 is A
    for letter in nums[8]:
        if letter in nums[1]:
            continue
        if letter in nums[4]:
            continue
        if letter not in nums[7]:
            continue
        a = letter
        break

    # everyone has F except 2

    for letter in letters:

        count = 0
        num2 = -1

        for v in i:
            if letter in v:
                count += 1
            else:
                num2 = v

        if count == 9:
            f = letter
            nums[2] = num2
            break

    ii.remove(nums[2])

    # C is the remaining letter in 7

    for letter in nums[7]:
        if not letter == f and not letter == a:
            c = letter

    # get num 3 from the 5 segments

    for v in ii:
        if len(v) == 5:
            # 2, 3, 5
            if a in v and c in v and f in v:
                nums[3] = v
                break

    ii.remove(nums[3])

    # get 5 by elimination

    for v in ii:
        if len(v) == 5:
            nums[5] = v
            break

    ii.remove(nums[5])

    # get 6 by elimination

    for v in ii:
        if len(v) == 6:
            if c not in v:
                nums[6] = v
                break

    ii.remove(nums[6])

    zeroOrNine = ii[0]

    isNine = True

    for letter in nums[4]:
        if letter not in zeroOrNine:
            isNine = False
            break

    if isNine:
        nums[9] = ii[0]
        nums[0] = ii[1]
    else:
        nums[0] = ii[0]
        nums[9] = ii[1]

    for v in range(0, 4):

        output = o[v]

        for i in range (0, 10):
            n = nums[i]
            if len(output) == len(n):
                match = True
                for c in n:
                    if c not in output:
                        match = False
                        break

                if match:         
                    sum += i * pow(10, 3 - v)
                    break

print(sum)
