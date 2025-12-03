if __name__ == '__main__':
    with open('input/2_1.txt', 'r') as file:
        line = file.readline()
        ranges = line.strip().split(',')
        invalid_total = 0
        for r in ranges:
            start, end = map(int, r.split('-'))

            for num in range(start, end + 1):
                str_num = str(num)
                if len(str_num) % 2 == 1:
                    continue
                front_half = str_num[:len(str_num)//2]
                back_half = str_num[len(str_num)//2:]
                if front_half != back_half:
                    continue
                invalid_total += num

        print(invalid_total)
