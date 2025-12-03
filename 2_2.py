if __name__ == '__main__':
    with open('input/2_2.txt', 'r') as file:
        line = file.readline()
        ranges = line.strip().split(',')
        invalid_total = 0
        for r in ranges:
            start, end = map(int, r.split('-'))
            seen = set()
            max_digits = len(str(end))

            for total_digits in range(2, max_digits + 1):
                for pattern_len in range(1, total_digits):
                    if total_digits % pattern_len != 0:
                        continue

                    reps = total_digits // pattern_len
                    if reps < 2:
                        continue

                    multiplier = sum(10 ** (pattern_len * i) for i in range(reps))
                    pattern_start = 10 ** (pattern_len - 1) if pattern_len > 1 else 1
                    pattern_end = 10 ** pattern_len

                    for pattern in range(pattern_start, pattern_end):
                        num = pattern * multiplier
                        if start <= num <= end and num not in seen:
                            seen.add(num)
                            invalid_total += num

        print(invalid_total)
