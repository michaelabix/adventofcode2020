import re
from collections import Counter

lists = []
num = 0
total = 0

def main():
	file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
	#part 1
	lists.append("")
	global total
	for line in file_puzzle_input:
		if re.match('^$',line):
			global num
			num += 1
			lists.append("")
		else:
			lists[num] = lists[num] + line.strip() + ' '

	for n in lists:
		n = n.replace(" ", "")
		unique = list(set(n))
		total += len(unique)
	print("the total number for part 1 is " + str(total))

	#part 2
	#reset total
	total = 0
	for n in lists:
		individual = n.split(' ')
		individual.pop()
		length = len(individual)
		chars = Counter(n.replace(" ", "")).most_common()
		for key, value in chars:
			if value == length:
				total += 1

	print("the total number for part 2 is " + str(total))

if __name__ == "__main__":
	main()
