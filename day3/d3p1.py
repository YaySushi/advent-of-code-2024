def read_file_and_answer(file_path):
    inp = ''
    with open(file_path, 'r') as file:
        for line in file:
            inp += line
    return sum_of_muls(inp)

import re
def sum_of_muls(mess):
    regex = '[m][u][l][(][0-9]{1,3}[,][0-9]{1,3}[)]'
    muls = re.findall(regex, mess)
    ans = 0

    for exp in muls:
        [left, right] = list(map(int, exp[4:-1].split(',')))
        ans += left * right
        
    return ans


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)