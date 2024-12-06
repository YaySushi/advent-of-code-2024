from collections import defaultdict
from functools import cmp_to_key

def read_file_and_answer(file_path):
	rules, updates = [], []
	with open(file_path, 'r') as file:
		for line in file:
			l = line.strip()
			if '|' in l: rules.append(list(map(int, l.split('|'))))
			elif len(l) > 0: updates.append(list(map(int, l.split(','))))
	return correct_fixed_updates(rules, updates)

def correct_fixed_updates(rules, updates):
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

		if invalid:
			# https://stackoverflow.com/questions/11850425/custom-python-list-sorting
			# just need to sort according to the rules given
			cmp_items = lambda a, b : 1 if b in bad[a] else -1
			cmp_items_py3 = cmp_to_key(cmp_items) # god bless functools
			update.sort(key=cmp_items_py3)
			ans += update[len(update) // 2]

	return ans


file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)