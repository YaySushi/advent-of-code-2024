import math

def bina(st):
	return ' '.join(format(ord(x), 'b') for x in str(st))

def read_file_and_answer(file_path):
	with open(file_path, 'r') as file:
		line = file.readline().strip()
		rA = int(line[12:])

		line = file.readline().strip()
		rB = int(line[12:])

		line = file.readline().strip()
		rC = int(line[12:])

		line = file.readline().strip()
		line = file.readline().strip()
		program = line[9:].split(',')

		program = list(map(int, program))
		return findRegA(program, rA, rB, rC)

def findRegA(program, rA, rB, rC):
	# perform a bfs to find all possible triplet of bits
	# for each segment for rA

	# first we analyze the input. we see that
	# the instruction 0,3 (in my input) divides rA by 8, which
	# is equivalent to shifting A to the right by 3.
	# there are 8 possible values for the 3 last bits of rA
	# the last 3 bits of rA form a number that is <= 7. 
	# the instruction 0,3 will make rA = 0 making it the last iteration.
	# finding the last 3 bits of rA will make the program output its 
	# last instruction (operand in this case). 

	# repeating the above for the 2nd last three bits, we get the last
	# 6 bits of rA which will make the program output its last two 
	# instructions. 

	# repeating this for every triplet of bits in rA we will get a value of
	# rA that will make the program output itself. 

	# there are some triplet of bits that work at a certain stage, but will
	# case a problem in the latter stages. to mitigate this, we perform a bfs
	# tracking all possible rA values so far. one of them will lead 
	# to a correct answer. 

	# an element (rA_so_far, b) of our queue will represent the value of rA
	# that makes the program output its last program[n-b+1:] characters.
	# (hopefully i don't have an off by one in that index expression...)

	n = len(program)
	qu = [(0, 1)]

	while len(qu) > 0:
		rA_so_far, b = qu.pop(0)

		# program has 16 instructions. when this element was pushed, the value of b
		# was 16. we got a program output matching program[16-17+1:] = program[0:]
		# which is exactly what we want as the output.
		if b == 17: return rA_so_far

		# the target portion of the program that we want outputted at this stage
		target = ','.join(list(map(str, program[n-b:])))

		# with 3 bits, values 0-7 can be represented.
		for i in range(0, 8):
			# "rA_so_far << 3" will shift rA_so_far to the left by 3
			# "+ i" will add the 3 least significant bits.
			if target == program_output(program, (rA_so_far << 3) + i, rB, rC):
				qu.append((8 * rA_so_far + i, b + 1))
	
	# sadness
	return ':('

def program_output(program, rA, rB, rC):
	regs = {'A': rA, 'B': rB, 'C': rC, 'out': ''}

	def combo(operand):
		if 0 <= operand <= 3: return operand
		# else: return [rA, rB, rC][operand - 4]
		elif operand == 4: return regs['A']
		elif operand == 5: return regs['B']
		elif operand == 6: return regs['C']
		else: return -1
	
	def adv(ip, operand):
		num = regs['A']
		den = 1 << combo(operand)
		res = num // den
		regs['A'] = res
		return ip + 2

	def bxl(ip, operand):
		res = regs['B'] ^ operand
		regs['B'] = res
		return ip + 2
	
	def bst(ip, operand):
		res = combo(operand) % 8
		regs['B'] = res
		return ip + 2
	
	def njz(ip, operand):
		if regs['A'] == 0: return ip + 2
		return operand
	
	def bxc(ip, operand):
		res = regs['B'] ^ regs['C']
		regs['B'] = res
		return ip + 2
	
	def out(ip, operand):
		res = combo(operand) % 8
		if len(regs['out']) > 0: regs['out'] += ','
		regs['out'] += str(res)
		return ip + 2
	
	def bdv(ip, operand):
		num = regs['B']
		den = 2 ** combo(operand)
		res = num // den
		regs['B'] = res
		return ip + 2
	
	def cdv(ip, operand):
		num = regs['A']
		den = 2 ** combo(operand)
		res = num // den
		regs['C'] = res
		return ip + 2
	
	instructions = {
		0: adv, 
		1: bxl,
		2: bst,
		3: njz,
		4: bxc,
		5: out,
		6: bdv,
		7: cdv
	}

	curr_ip = 0
	while curr_ip < len(program):
		opcode = program[curr_ip]
		operand = program[curr_ip + 1]
		instruction = instructions[opcode]
		curr_ip = instruction(curr_ip, operand)
	
	return regs['out']

file_path = 'input.txt'
ans = read_file_and_answer(file_path)
print(ans)