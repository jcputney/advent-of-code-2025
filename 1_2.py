START_POS = 50
DIGITS = 100

if __name__ == '__main__':
    with open('input/1_2.txt', 'r') as file:
        lines = file.readlines()
        current_pos = START_POS
        count = 0
        line_num = 0
        for line in lines:
            clicks = int(line.strip().replace('L', '-').replace('R', ''))
            next_pos = (current_pos + clicks)
            zeros = abs(int(next_pos / 100)) + (1 if (current_pos < 0 < next_pos) or (next_pos < 0 < current_pos) or next_pos == 0 else 0)
            current_pos = (next_pos + (zeros * DIGITS)) % DIGITS
            count += zeros

        print(count)
