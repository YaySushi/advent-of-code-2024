def read_file_and_answer(file_path):
    grid = []
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    return x_mas_count(grid)

def x_mas_count(grid):
    n = len(grid)
    m = len(grid[0])
    ans = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 'A':
                corners = grid[i-1][j-1] + grid[i-1][j+1] + grid[i+1][j+1] + grid[i+1][j-1]
                if corners in {'MMSS', 'SMMS', 'SSMM', 'MSSM'}: ans += 1
    return ans


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)