def read_file_and_answer(file_path):
    inp = ''
    with open(file_path, 'r') as file:
        for line in file:
            inp += line
    return sum_of_conditional_muls(inp)

import re
def sum_of_conditional_muls(mess):
    mul_regex = "[m][u][l][(][0-9]{1,3}[,][0-9]{1,3}[)]"
    do_regex = "[d][o][(][)]"
    dont_regex = "[d][o][n]['][t][(][)]"
    regex = mul_regex + '|' + do_regex + '|' + dont_regex

    muls = re.findall(regex, mess)
    ans = 0
    do = True

    for exp in muls:
        if len(exp) > 7: 
            [left, right] = list(map(int, exp[4:-1].split(',')))
            if do: ans += left * right
        else: do = len(exp) == 4
        
    return ans


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)