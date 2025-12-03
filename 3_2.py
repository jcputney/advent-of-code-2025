NUM_DIGITS = 12

if __name__ == '__main__':
    with open('input/3_2.txt', 'r') as file:
        lines = file.readlines()
        total = 0

        digits = list(range(NUM_DIGITS))
        for line in lines:
            line = line.strip()
            digits[0] = int(line[0])
            idx = 0
            for i in range(1, len(line) - (NUM_DIGITS - 1)):
                if int(line[i]) > digits[0]:
                    digits[0] = int(line[i])
                    idx = i
            for n in range(1, NUM_DIGITS):
                digits[n] = -1
                for i in range(idx + 1, len(line) - (NUM_DIGITS - n - 1)):
                    if int(line[i]) > digits[n]:
                        digits[n] = int(line[i])
                        idx = i

            line_total = 0
            for n in range(NUM_DIGITS):
                line_total = (line_total * 10) + digits[n]
            total += line_total

        print(total)

