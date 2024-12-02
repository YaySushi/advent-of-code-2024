def read_file_and_answer(file_path):
    A, B = [], []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            A.append(left)
            B.append(right)
    return distance(A, B)


def distance(A, B):
    return sum([abs(b - a) for (a, b) in zip(sorted(A), sorted(B))])


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)