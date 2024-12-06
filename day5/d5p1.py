from collections import defaultdict

def read_file_and_answer(file_path):
	rules, updates = [], []
	with open(file_path, 'r') as file:
		for line in file:
			l = line.strip()
			if '|' in l: rules.append(list(map(int, l.split('|'))))
			elif len(l) > 0: updates.append(list(map(int, l.split(','))))
	return correct_updates(rules, updates)

def correct_updates(rules, updates):
	ans = 0
	bad = defaultdict(set)
	
	# a must come before b, if it does.
	# a can not appear after b
	for [a, b] in rules: bad[b].add(a)
		
	for update in updates:
		# check if there is any invalid pair of pages.
		invalid = False
		for i in range(len(update)):
			if invalid: break
			for j in range(i + 1, len(update)):
				if invalid: break
				if update[j] in bad[update[i]]: invalid = True

		if invalid: continue
		ans += update[len(update) // 2]

	return ans


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)