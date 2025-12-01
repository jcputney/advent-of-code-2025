START_POS = 50
DIGITS = 100

if __name__ == '__main__':
    with open('input/1_1.txt', 'r') as file:
        lines = file.readlines()
        current_pos = START_POS
        count = 0
        for line in lines:
            clicks = int(line.strip().replace('L', '-').replace('R', ''))
            clicks = (clicks % DIGITS) if clicks > 0 else (clicks % -DIGITS)
            next_pos = (current_pos + clicks)
            current_pos = 100 + next_pos if next_pos < 0 else next_pos % DIGITS
            if current_pos == 0:
                count += 1

        print(count)
