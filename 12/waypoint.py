import re

#file shenanigans
file_puzzle_input = open("puzzle_input", 'r').read().splitlines()

#global list
instructions = []

#ship object
class ship():
	def __init__(self):
		self.north_south = 0
		self.east_west = 0

#parse file input
def parse_input():
	for f in file_puzzle_input:
		temp = re.compile("([a-zA-Z]+)([0-9]+)")
		instructions.append(temp.match(f).groups())

#trigger navigation
def navigate(ferry, waypoint):
	for i in instructions:
		if i[0] == 'R' or i[0] == 'L':
			rotate(i[0], int(i[1]), waypoint)
		elif i[0] == 'F':
			forward(ferry, waypoint, int(i[1]))
		else:
			compass_points(waypoint, i[0], int(i[1]))

#rotate either clockwise or counter clockwise
def rotate(dir, num, waypoint):
	temp_east = waypoint.east_west
	temp_north = waypoint.north_south
	if dir == 'L':
		if num == 90:
			waypoint.north_south = temp_east
			waypoint.east_west = -temp_north
		elif num == 180:
			waypoint.north_south = -temp_north
			waypoint.east_west = -temp_east
		elif num == 270:
			waypoint.north_south = -temp_east
			waypoint.east_west = temp_north
	if dir == 'R':
		if num == 90:
			waypoint.north_south = -temp_east
			waypoint.east_west = temp_north
		elif num == 180:
			waypoint.north_south = -temp_north
			waypoint.east_west = -temp_east
		elif num == 270:
			waypoint.north_south = temp_east
			waypoint.east_west = -temp_north

#move forward
def forward(ferry, waypoint, num):
	ferry.east_west += num * waypoint.east_west
	ferry.north_south += num * waypoint.north_south

#move according to compass points
def compass_points(waypoint, dir, num):
	if dir == 'N':
		waypoint.north_south += num
	elif dir == 'S':
		waypoint.north_south -= num
	elif dir == 'E':
		waypoint.east_west += num
	elif dir == 'W':
		waypoint.east_west -= num

#find total
def total(ferry):
	return abs(ferry.north_south) + abs(ferry.east_west)

def main():
	ferry1 = ship()
	waypoint1 = ship()
	waypoint1.east_west = 10
	waypoint1.north_south = 1
	parse_input()
	navigate(ferry1,waypoint1)
	print("the answer for part 2 is " + str(total(ferry1)))
if __name__ == "__main__":
	main()
