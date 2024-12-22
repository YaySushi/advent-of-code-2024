from collections import defaultdict

def read_file_and_answer(file_path):
    secrets = []
    with open(file_path, 'r') as file:
        for line in file:
            if line != '': 
                   secrets.append(int(line.strip()))
    return get_banana_rich(secrets)

def get_banana_rich(secrets):
    rounds = 2000

    # calculate sequence of prices for each buyer
    prices = []
    for i in range(len(secrets)):
        prices.append([])
        for k in range(rounds):
            prices[i].append(secrets[i] % 10)
            secrets[i] = next_secret(secrets[i])
    
    # dictionary that will map a sequence to banana earnings
    change_seqs_earnings = defaultdict(int)

    for price_seq in prices:
        # compute sequence of changes between each price.
        # first index will not be used, but fill it in for convenience
        changes = [float('inf')]
        for i in range(1, len(price_seq)):
            changes.append(price_seq[i] - price_seq[i - 1])
        
        # for every sequence of 4 changes, update change_seqs_earnings dictionary
        # stating how many bananas this sequenc earns us
        # seen_seqs makes sure we only take first price in this price_seq
        seen_seqs = set()
        for i in range(1, len(changes) - 3):
            change_seq = tuple(changes[i:i+4])
            if change_seq not in seen_seqs:
                change_seqs_earnings[change_seq] += price_seq[i + 3]
                seen_seqs.add(change_seq)
    
    most_bananas = -1
    for change_seq in change_seqs_earnings.keys():
        most_bananas = max(most_bananas, change_seqs_earnings[change_seq])

    return most_bananas

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