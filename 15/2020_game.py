file_puzzle_input = open("puzzle_input", 'r').read().strip().split(',')


def game(end):
	# assign variables
	used = {}
	index = 0
	num = 0
	next = 0
	first = 0

	#loop through to number
	while index < end:
		#add starting numbers to dict
		if not used:
			for f in file_puzzle_input:
				used.update({int(f): index})
				first = 1
				index += 1
		#otherwise play game 
		else:
			#last number was used for the first time
			if first == 1:
				num = 0
				next = index - used.get(num)
				used.update({num: index})
				first = 0

			#otherwise do some math
			else:
				num = next
				if num in used:
					next = index - used.get(num)
					used.update({num: index})
					first = 0
				else:
					used.update({num: index})
					first = 1
			index += 1
	return num

def main():
	print("the answer to part 1 is: " + str(game(2020)))
	print("the answer to part 2 is: " + str(game(30000000)))

if __name__ == "__main__":
	main()
