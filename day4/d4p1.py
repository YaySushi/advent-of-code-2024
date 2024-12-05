def read_file_and_answer(file_path):
    grid = []
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    return xmas_count(grid)

def xmas_count(grid):
    n = len(grid)
    m = len(grid[0])
    ans = 0

    for i in range(n):
        for j in range(m):
            # horizontal
            if j + 3 < n:
                word = grid[i][j:j+4]
                if word in targets: ans += 1
            # vertical
            if i + 3 < m:
                word = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]
                if word in targets: ans += 1
            # diagonal \
            if i + 3 < n and j + 3 < m:
                word = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3]
                if word in targets: ans += 1
            # diagonal /
            if 3 <= i and j + 3 < m:
                word = grid[i][j] + grid[i-1][j+1] + grid[i-2][j+2] + grid[i-3][j+3]
                if word in targets: ans += 1
    return ans


targets = {'XMAS', 'SAMX'}
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)