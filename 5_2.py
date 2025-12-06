if __name__ == '__main__':
    with open('input/5_2.txt', 'r') as file:
        ranges = []
        while True:
            line = file.readline()
            line = line.strip()
            if line == '':
                break
            parts = line.split('-')
            ranges.append((int(parts[0]), int(parts[1])))

        ranges = sorted(ranges, key=lambda x: x[0])

        for idx, r in enumerate(ranges):
            c_start, c_end = r
            if idx < len(ranges) - 1:
                n_start, n_end = ranges[idx + 1]
                if c_end >= n_start:
                    new_range = (c_start, max(c_end, n_end))
                    ranges[idx + 1] = new_range
                    ranges[idx] = None

        ranges = [r for r in ranges if r is not None]

        total = 0
        for r in ranges:
            total += r[1] - r[0] + 1

        print(total)



