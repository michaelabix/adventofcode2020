#open file
file_object = open("puzzle_input", 'r')

#read lines & remove newline
lines = file_object.readlines()
new_lines= [a[:-1] for a in lines]

#part 1
for x in new_lines:
	for y in new_lines:
		n = int(x) + int(y)
		if n == 2020:
			print "part 1:"
			print(int(x) * int(y))
			break
	else:
		continue
	break

#part 2
for x in new_lines:
	for y in new_lines:
		for z in new_lines:
			n = int(x) + int(y) + int(z)
			if n == 2020:
				print "part 2:"
				print(int(x) * int(y) * int(z))
				break
		else:
			continue
		break
	else:
		continue
	break

