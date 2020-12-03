from collections import Counter

#file shenanigans
file_object = open("puzzle_input", 'r').read().splitlines()

#counter
i = 0

#part 1
for line in file_object:
	list = line.split(" ")
	policy = list[0].split("-")
	letter = list[1].split(":")
	password = list[2]
	counted_string = (Counter(password))
	for x, y in counted_string.items():
		if x == letter[0]:
			if y >= int(policy[0]) and y <= int(policy[1]):
				i += 1
			break
		else:
			continue
print "the number for part 1 is:"
print i

#reset counter
i = 0

#part 2
for line in file_object:
	list = line.split(" ")
	policy = list[0].split("-")
	letter = list[1].split(":")
	password = list[2]
	min = int(policy[0]) - 1
	max = int(policy[1]) - 1
	minimum = 0 
	maximum = 0

	if (password[min] == letter[0]) and (policy[0] != 0):
		minimum = 1
		
	if password[max] == letter[0]:
		maximum = 1
		
	if (minimum == 1 and maximum == 0):
		i += 1
	
	if (minimum == 0 and maximum == 1):
		i += 1

		
print "the number for part 2 is:"
print i