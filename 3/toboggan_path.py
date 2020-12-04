#file shenanigans
file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
file_right = open("right", 'r').read().splitlines()
file_down = open("down", 'r').read().splitlines()

#part 1

#initialize variables
line_pos = 3 
slope = 3
line_length = len(file_puzzle_input[0]) - 1
trees = 0

#loop through file input to identify trees
for line in file_puzzle_input[1:]:
	line_length = len(line) - 1
	if(line_pos > line_length):
		line_pos = line_pos - line_length -1
	if line[line_pos] == '#':
		trees += 1
	line_pos = line_pos + slope

print "the number of trees for part 1 is:"
print trees

#part 2

#initialize variables
counter = 0
trees_list = []

#loop n items in slope requirements
for n in file_right:
	line_length = len(file_puzzle_input[0]) - 1
	line_pos = int(file_right[counter])
	slope = int(file_right[counter])
	skip = int(file_down[counter])
	trees = 0
	#loop through puzzle input and identify trees
	for line in file_puzzle_input[skip::skip]:
        	line_length = len(line) - 1
        	if(line_pos > line_length):
                	line_pos = line_pos - line_length -1
        	if line[line_pos] == '#':
                	trees += 1
        	line_pos = line_pos + slope
	#add tree total to array for each iteration of loop
	if trees > 0:
		trees_list.append(trees)	
	counter += 1

#reset counter and set starting total
counter = 1
total = trees_list[0]
#loop through tree array and do some math
for t in trees_list[1:]:
	total = total * trees_list[counter]
	counter += 1

print "the total number of trees for part 2 is:"
print total 

