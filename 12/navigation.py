import re

#file shenanigans
file_puzzle_input = open("puzzle_input", 'r').read().splitlines()

#global list
instructions = []

#ship object
class ship():
	def __init__(self):
		self.direction = "east"
		self.north_south = 0
		self.east_west = 0

#parse file input
def parse_input():
	for f in file_puzzle_input:
		temp = re.compile("([a-zA-Z]+)([0-9]+)")
		instructions.append(temp.match(f).groups())

#trigger navigation
def navigate(ferry):
	for i in instructions:
		if i[0] == 'R' or i[0] == 'L':
			rotate(i[0], int(i[1]), ferry)
		elif i[0] == 'F':
			forward(ferry, int(i[1]))
		else:
			compass_points(ferry, i[0], int(i[1]))

#rotate either clockwise or counter clockwise
def rotate(dir, num, ferry):
	directions = ['north', 'east', 'south', 'west']
	index = directions.index(ferry.direction)
	new_dir = 0
	if num == 90:
		if dir == 'R':
			new_dir = index + 1
		else:
			new_dir = index - 1
	elif num == 180:
		if dir == 'R':
			new_dir = index + 2
		else:
			new_dir = index - 2
	elif num == 270:
		if dir == 'R':
			new_dir = index + 3
		else:
			new_dir = index - 3

	if dir == 'R' and new_dir > 3:
		new_dir = new_dir - len(directions)

	ferry.direction = directions[new_dir]

#move forward
def forward(ferry, num):
	direction = ferry.direction
	if direction == "east" or direction == "north":
		if direction == "north":
			ferry.north_south += num
		else:
			ferry.east_west += num

	else:
		if direction == "south":
			ferry.north_south -= num
		else:
			ferry.east_west -= num

#move according to compass points
def compass_points(ferry, dir, num):
	if dir == 'N':
		ferry.north_south += num
	elif dir == 'S':
		ferry.north_south -= num
	elif dir == 'E':
		ferry.east_west += num
	elif dir == 'W':
		ferry.east_west -= num

#find total
def total(ferry):
	return abs(ferry.north_south) + abs(ferry.east_west)

def main():
	ferry1 = ship()
	parse_input()
	navigate(ferry1)
	print("the answer for part 1 is " + str(total(ferry1)))
if __name__ == "__main__":
	main()
