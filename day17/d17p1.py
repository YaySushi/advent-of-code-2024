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
		program = list(map(int, line[9:].split(',')))

		return program_output(program, rA, rB, rC)

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