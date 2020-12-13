file_puzzle_input = open("puzzle_input", 'r').read().splitlines()

#global variables
seats = []
no_swap = 0

#define seat objects
class seat():
	def __init__(self):
		type = 0
		occupied = 0
		swap = 0

#parse input
def create_seats():
	for f in file_puzzle_input:
		seats.append([])
		item = list(f)
		for i in item:
			new_seat = seat()
			new_seat.type = i
			new_seat.occupied = 0
			new_seat.swap = 0
			seats[-1].append(new_seat)
	
#find adjacent for part 1
def find_adjacent(x,y):
	swap = 0
	startx = x - 1
	while startx <= (x + 1):
		starty = y - 1
		while starty <= (y + 1):
			if startx < 0 or startx >= len(seats):
				break
			if starty >= len(seats[x]):
				break
			if starty < 0:
				starty += 1
				continue
			if not (startx == x and starty == y):
				if (seats[startx][starty].occupied == 1) and (seats[startx][starty].type != "."):
					swap += 1
			starty += 1
		startx += 1
	return(swap)

#find seats in view for part 2. this is messy and could benefit from a switch statement
def find_in_view(x,y):
	swap = 0
	#check up
	up = x - 1
	down = x + 1
	left = y - 1
	right = y + 1
	d_up = up
	d_up2 = up
	d_down = down
	d_down2 = down
	d_left = left
	d_left2 = left
	d_right = right
	d_right2 = right

	#check up
	while up >= 0:
		seat_type = seats[up][y].type
		if seat_type == '#':
			swap += 1
			break
		elif seat_type == 'L':
			break
		up -= 1
	#check down 
	while down < len(seats):
		seat_type = seats[down][y].type
		if seat_type == '#':
			swap += 1
			break
		elif seat_type == 'L':
			break
		down += 1
	#check left
	while left >= 0:
		seat_type = seats[x][left].type
		if seat_type == '#':
			swap += 1
			break
		elif seat_type == 'L':
			break
		left -= 1
	#check right
	while right < len(seats[x]):
		seat_type = seats[x][right].type
		if seat_type == '#':
			swap += 1
			break
		elif seat_type == 'L':
			break
		right += 1
	#check diagonals
	while d_up >= 0 and d_left >= 0:
		seat_type = seats[d_up][d_left].type
		if seat_type == '#':
			swap += 1
			break
		elif seat_type == 'L':
			break
		d_up -= 1
		d_left -= 1

	while d_up2 >= 0 and d_right2 < len(seats[d_up2]):
		seat_type = seats[d_up2][d_right2].type
		if seat_type == '#':
			swap += 1
			break
		elif seat_type == 'L':
			break
		d_up2 -= 1
		d_right2 += 1

	while d_down2 < len(seats) and d_left2 >= 0:
		seat_type = seats[d_down2][d_left2].type
		if seat_type == '#':
			swap += 1
			break
		elif seat_type == 'L':
			break
		d_down2 += 1
		d_left2 -= 1
	
	while d_down < len(seats) and d_right < len(seats[d_down]):
		seat_type = seats[d_down][d_right].type
		if seat_type == '#':
			swap += 1
			break
		elif seat_type == 'L':
			break
		d_down += 1
		d_right += 1
	return(swap)

#iterates through 2 dimensional array and applies operations based on whether it was called by part 1 or part 2. this is slow. 
def swap_seats(part):
	global no_swap
	rows = len(seats)
	x = 0
	while x < rows:
		columns = len(seats[x])
		y = 0
		while y < columns:
			if seats[x][y].type != ".":
				if part == 1:
					adjacent = find_adjacent(x,y)
					if adjacent == 0 and seats[x][y].type == 'L':
						seats[x][y].swap = 1
					if adjacent >= 4 and seats[x][y].type == '#':
						seats[x][y].swap = 1
				if part == 2:
					in_view = find_in_view(x,y)
					if in_view == 0 and seats[x][y].type == 'L':
						seats[x][y].swap = 1
					if in_view >= 5 and seats[x][y].type == '#':
						seats[x][y].swap = 1
			y += 1
		x+= 1
	test_swap = 0
	for s in seats:
		for i in s:
			if i.swap == 1:
				if i.type == "#":
					i.type = "L"
					i.occupied = 0
					i.swap = 0
				elif i.type == "L":
					i.type = "#"
					i.occupied = 1
					i.swap = 0
				test_swap += 1
	if test_swap == 0:
		no_swap = 1

#finds the total number of occupied seats at the end
def find_total():
	total = 0
	for s in seats:
		for i in s:
			if i.occupied == 1:
				total += 1
	return total

def main():
	global no_swap
	global seats
	create_seats()

	#part 1
	while no_swap == 0:
		swap_seats(1)
	print("the answer to part 1 is " + str(find_total()))
	#reset
	seats = []
	create_seats()
	no_swap = 0

	#part 2
	while no_swap == 0:
		swap_seats(2)
	print("the answer to part 2 is " + str(find_total()))

if __name__ == "__main__":
	main()
