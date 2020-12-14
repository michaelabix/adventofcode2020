file_puzzle_input = open("puzzle_input", 'r').read().splitlines()

#read input
def parse():
	timestamp = file_puzzle_input[0]
	bus_id = file_puzzle_input[1]
	bus_list = bus_id.split(',')
	return timestamp, bus_list

#find product
def multiply(id,time):
	product = 0
	n = 0
	while product < time:
		product = n * id
		n += 1
	return product

#find earliest timestamp
def part2(busses):
	n = 0
	t = 0
	inc = 1
	for i,b in enumerate(busses):
		if b == "x":
			continue
		while ((t + i) % int(b)) != 0:
			t += inc
		inc *= int(b)
	return t

def main():
	#declare variables
	arrival, busses = parse()
	num = {}

	#part 1
	for b in busses:
		if b == "x":
			continue
		else:
			temp_num = multiply(int(b),int(arrival))
			if temp_num >= int(arrival):
				num.update({b: temp_num})

	lowest = min(num.values())
	bus = [key for key in num if num[key] == lowest]
	bus = bus[0]
	diff = int(num.get(bus)) - int(arrival)
	mult = diff * int(bus)
	print("the bus ID is: " + str(bus))
	print("the time difference is: " + str(mult))

	#part 2
	p2_timestamp = part2(busses)
	print("part 2 earliest timestamp: " + ' ' + str(p2_timestamp))

if __name__ == "__main__":
	main()
