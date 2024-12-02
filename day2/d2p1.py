def read_file_and_answer(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(list(map(int, line.split())))
    return safe_count(lines)

def safe_count(lines):
    return [line_safe(line) for line in lines].count(True)

def line_safe(line):
    n = len(line)
    rule_inc = all([line[i] >= line[i - 1] for i in range(1, n)])
    rule_dec = all([line[i] <= line[i - 1] for i in range(1, n)])
    rule_diff = all([1 <= abs(line[i] - line[i - 1]) <= 3 for i in range(1, n)])
    return (rule_inc or rule_dec) and rule_diff


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)