DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
if __name__ == '__main__':
    with open('input/4_2.txt', 'r') as file:
        grid = []
        for line in file:
            row = []
            for c in line.strip():
                row.append(c)
            grid.append(row)

        total = 0
        removed = -1
        while removed != 0:
            removed = 0
            for i, row in enumerate(grid):
                for j, pos in enumerate(row):
                    if pos == '@':
                        count = 0
                        for d in DIRS:
                            ni, nj = i + d[0], j + d[1]
                            if 0 <= ni < len(grid) and 0 <= nj < len(row):
                                if grid[ni][nj] == '@':
                                    count += 1
                        if count < 4:
                            removed += 1
                            grid[i][j] = '.' # remove isolated '@'
                            total += 1
        print(total)
