import math

#declare global variables
min_row = 0
max_row = 127
min_seat = 0
max_seat = 7
multiply = 8
row = []
seat = []
length = 10
seat_location = open("puzzle_input", 'r').read().splitlines()

#calculate seat ID
def find_seatid(location):
	if len(location) > length:
		print "this is not a valid seat ID"
	else:
		#parse seat code
		row_string = location[:-3]
		seat_string = location[-3:]
		minr = float(min_row)
		maxr = float(max_row)
		mins = float(min_seat)
		maxs = float(max_seat)

		#find median and take ceiling and floor into consideration
		for x in row_string:
			if x == 'B':
				medianr = math.ceil((minr + maxr) / 2)
				minr = medianr
				row_num = medianr
			elif x == 'F':
				medianr = math.floor((minr + maxr) / 2)
				maxr = medianr
				row_num = medianr
		for y in seat_string:
			if y == 'R':
				medians = math.ceil((mins + maxs) / 2)
				mins = medians
				seat_num = medians
			elif y == 'L':
				medians = math.floor((mins + maxs) / 2)
				maxs = medians
				seat_num = medians

		#cast floats as ints & return results
		row_num = int(row_num)
		seat_num = int(seat_num)
		return row_num,seat_num

#find max seat number for part 1
def find_max():
	max = 0
	for i,n in enumerate(row):
		seatID = get_seatID(n,seat[i])
		if seatID > max:
			max = seatID
	return max

#do some math to calculate ID
def get_seatID(x,y):
	seatID = int(x) * multiply + int(y)
	return seatID

#locate seat for part 2
def find_seat():
	seats = []
	for i,n in enumerate(row):
		seats.append(get_seatID(n,seat[i]))
	sorted_seats = sorted(seats)
	previous_seat = 0
	my_seat = 0
	for s in sorted_seats:
		if previous_seat != 0:
			if s != previous_seat + 1:
				my_seat = previous_seat + 1
				break
			else:
				previous_seat = s
		else:
			previous_seat = s
	return my_seat

#set seating
def set_seating():
	for location in seat_location:
                seating = find_seatid(location)
                row.append(seating[0])
                seat.append(seating[1])

def main():

	set_seating()
	
	#part 1
	print "the highest seat number for part 1 is " + str(find_max())

	#part 2
	print "the seat number for part 2 is " + str(find_seat())

if __name__ == "__main__":
	main()
