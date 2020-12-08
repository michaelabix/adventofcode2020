file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
instructions = []
accumulator = 0

class instruction():
	def __init__(self):
		self.instruction = ""
		self.num = 0
		self.times_run = 0

def parse_input():
	for f in file_puzzle_input:
		new_instruction = instruction()
		temp = f.split(' ')
		new_instruction.instruction = temp[0]
		new_instruction.num = int(temp[1])
		instructions.append(new_instruction)
		
def operations():
	global accumulator
	i = 0
	length = len(instructions)
	loop = 0
	while i < length:
		if instructions[i].times_run == 1:
			loop = 1
			break
		if instructions[i].instruction == "jmp":
			instructions[i].times_run += 1
			i += instructions[i].num
		elif instructions[i].instruction == "acc":
			accumulator += instructions[i].num
			instructions[i].times_run += 1
			i += 1
		else:
			instructions[i].times_run += 1
			i += 1
	return loop

def reset():
	global accumulator
	global instructions
	accumulator = 0
	for i in range(len(instructions)):
		instructions[i].times_run = 0

def fixed_operations():
	for x,i in enumerate(instructions):
		reset()
		if (i.instruction == "jmp") or (i.instruction == "nop" and i.num != 0):
			temp = i.instruction
			if i.instruction == "jmp":
				instructions[x].instruction = "nop"
			else:
				instructions[x].instruction = "jmp"
			complete = operations()
			instructions[x].instruction = temp
			if complete == 0:
				break

def main():
	parse_input()

	#part 1	
	operations()
	print("the answer for part 1 is: " + str(accumulator))

	#part 2
	reset()
	fixed_operations()
	print("the answer for part 2 is: " + str(accumulator))

if __name__ == "__main__":
	main()
