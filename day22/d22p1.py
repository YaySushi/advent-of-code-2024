def read_file_and_answer(file_path):
    secrets = []
    with open(file_path, 'r') as file:
        for line in file:
            if line != '': 
                   secrets.append(int(line.strip()))
    return sum_of_secrets(secrets)

def sum_of_secrets(secrets):
    for k in range(2000):
        for i in range(len(secrets)):
            secrets[i] = next_secret(secrets[i])
    return sum(secrets)

def next_secret(secret):
    modified_secret = secret * 64
    secret = mix_and_prune(secret, modified_secret)

    modified_secret = secret // 32
    secret = mix_and_prune(secret, modified_secret)

    modified_secret = secret * 2048
    secret = mix_and_prune(secret, modified_secret)

    return secret

def mix_and_prune(secret, mixee):
    return (secret ^ mixee) % 16777216



file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)