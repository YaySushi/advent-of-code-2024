def read_file_and_answer(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(list(map(int, line.split())))
    return safe_count(lines)

def safe_count(lines):
    ans = 0
    for line in lines:
        for i in range(len(line)):
            line_with_level_removed = line[:i] + line[i+1:]
            if line_safe(line_with_level_removed):
                ans += 1
                break
    return ans

def line_safe(line):
    n = len(line)
    rule_inc = all([line[i] >= line[i - 1] for i in range(1, n)])
    rule_dec = all([line[i] <= line[i - 1] for i in range(1, n)])
    rule_diff = all([1 <= abs(line[i] - line[i - 1]) <= 3 for i in range(1, n)])
    return (rule_inc or rule_dec) and rule_diff


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)