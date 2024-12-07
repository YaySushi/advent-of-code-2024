def read_file_and_answer(file_path):
	results = []
	terms = []
	with open(file_path, 'r') as file:
		for line in file:
			inp = line.split(': ')
			results.append(int(inp[0]))
			terms.append(list(map(int, inp[1].split(' '))))
	return calibration_result(results, terms)

def calibration_result(results, terms):
	sm = 0
	for (res, terms) in zip(results, terms):
		if valid_equation(res, terms): sm += res
	return sm

def valid_equation(res, terms):
	if len(terms) == 1: return res == terms[0]
		
	if valid_equation(res, [terms[0] + terms[1]] + terms[2:]): return True
	if valid_equation(res, [terms[0] * terms[1]] + terms[2:]): return True
	if valid_equation(res, [int(str(terms[0]) + str(terms[1]))] + terms[2:]): return True
	return False
	
file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)