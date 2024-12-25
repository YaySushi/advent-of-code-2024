def read_file_and_answer(file_path):
    keys = []
    locks = []
    with open(file_path, 'r') as file:
        grids = file.read().strip().split('\n\n')
        for grid in grids:
            # key
            if grid[0] == '.':
                keys.append(grid.split('\n'))
            # lock
            else:
                locks.append(grid.split('\n'))
    return fit_combos(keys, locks)

HEIGHT = 7
WIDTH = 5

def fit_combos(keys, locks):
    key_hts = grid_to_heights(keys)
    lock_hts = grid_to_heights(locks)

    ans = 0

    for key_ht in key_hts:
        for lock_ht in lock_hts:
            fit = True
            for col in range(WIDTH):
                if key_ht[col] + lock_ht[col] > HEIGHT:
                    fit = False
                    break
            if fit: ans += 1
            
    return ans

def grid_to_heights(grids):
    heights = []
    for grid in grids:
        height = []
        for col in range(WIDTH):
            num_slashes = 0
            for row in range(HEIGHT):
                if grid[row][col] == '#': num_slashes += 1
            height.append(num_slashes)
        heights.append(height)
    return heights

file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)