from collections import defaultdict

def read_file_and_answer(file_path):
	nums = []
	with open(file_path, 'r') as file:
		for line in file:
			nums = list(map(int, line.split()))
	return stone_count(nums)

def stone_count(nums):
	solved = defaultdict(dict)

	def change(num, rep):
		if rep == 0: return 1

		if num in solved:
			for (num_rep, num_count) in solved[num].items():
				if num_rep == rep: return num_count
		
		count = 0
		len_num = len(str(num))

		if num == 0: 
			count = change(1, rep - 1)
		elif len_num % 2 == 0:
			num_l = int(str(num)[:len_num//2])
			num_r = int(str(num)[len_num//2:])
			count = change(num_l, rep - 1) + change(num_r, rep - 1)
		else: 
			count = change(num * 2024, rep - 1)
	
		solved[num][rep] = count
		return count

	return sum([change(num, 25) for num in nums])



file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)