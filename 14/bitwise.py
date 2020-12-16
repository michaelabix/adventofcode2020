#import re
file_puzzle_input = open("puzzle_input2", 'r').read().splitlines()

def part1():
	memory = {}
	for f in file_puzzle_input:
		items = f.split(' ')
		if items[0] == "mask":
			mask = items[2]
			zeroes = mask.replace("X","0")
			ones = mask.replace("X","1")
		else:
			num = int(items[2])
			new_num = (num & int(ones, 2)) | int(zeroes, 2)
			memory.update({items[0]: new_num})

	return sum(memory.values())

#part 2 coming soon
def part2():
	pass

def main():
	print("the answer to part 1 is: " + str(part1()))
#	print("the answer to part 2 is: " + str(part2()))

if __name__ == "__main__":
	main()
