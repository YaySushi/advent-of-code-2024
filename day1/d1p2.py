def read_file_and_answer(file_path):
    A, B = [], []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            A.append(left)
            B.append(right)
    return similarity(A, B)


def similarity(A, B):
    return sum([a * B.count(a) for a in A])


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)

