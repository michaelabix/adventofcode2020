import re

#set global variables
file_puzzle_input = open("puzzle_input", 'r').read().split('\n\n')
rules = {}
tickets = []

#create objects for rules and tickets
class rule():
	def __init__(self):
		self.r1 = []
		self.r2 = []
		self.field = -1

class ticket():
	def __init__(self):
		self.nums = []
		self.not_valid = 0

#parse input
def parse():
	temp_rules = file_puzzle_input[0].split('\n')
	temp_my_ticket = file_puzzle_input[1].split('\n')[1:]
	temp_tickets = file_puzzle_input[2].split('\n')[1:-1]
	for r in temp_rules:
		temp = r.split(':')
		name = temp[0].strip(':')
		rule_obj = rule()
		numbers = re.findall('[0-9]+',temp[1])
		for i,n in enumerate(numbers):
			if i < 2:
				rule_obj.r1.append(n)
			else:
				rule_obj.r2.append(n)
		rules.update({name: rule_obj})

	my_ticket = ticket()
	my_ticket.nums = temp_my_ticket[0].split(',')
	for t in temp_tickets:
		new_ticket = ticket()
		new_ticket.nums = t.split(',')
		tickets.append(new_ticket)

	return my_ticket

#part 1
def scanning_error_rate():
	invalid = []
	for t in tickets:
		for n in t.nums:
			count = 0
			for x in rules.values():
				if (int(n) in range(int(x.r1[0]), int(x.r1[1]) + 1)) or (int(n) in range(int(x.r2[0]), int(x.r2[1]) + 1)):
					count += 1
			if count == 0:
				invalid.append(int(n))
				t.not_valid = 1
	total = 0
	for i in invalid:
		total += int(i)
	return total
	
#discover order and assign to rule object
def find_field_order():
	order = {}

	#loop until all values are found
	while len(order) != len(rules):

		#loop through rules
		for k in rules.keys():

			#test if already found
			if k in order.keys():
				continue
			else:
				options = set()

				#loop through tickets
				for t in tickets:
					
					#test if valid
					if t.not_valid == 1:
						continue
					else:
						possibilities = set()

						#loop through numbers in ticket
						for i,n in enumerate(t.nums):
							#test if in range
							if (int(n) in range(int(rules[k].r1[0]), int(rules[k].r1[1]) + 1)) or (int(n) in range(int(rules[k].r2[0]), int(rules[k].r2[1]) + 1)):
								if i not in order.values():
									possibilities.add(i)
					if not options:
						options = options.union(possibilities)
					if not possibilities:
						continue
					else:
						options = options.intersection(possibilities)
				if len(options) == 1:
					for o in options:
						rules[k].field = o
						order.update({k: o})		

#part 2 answer
def departure(ticket):
	find_field_order()
	total = 1
	for k in rules.keys():
		if re.match('^departure.*$',k):
			total *= int(ticket.nums[rules[k].field])
	return total
	
def main():
	my_ticket = parse()
	print("the answer to part 1 is: " + str(scanning_error_rate()))
	print("the answer to part 2 is: " + str(departure(my_ticket)))

if __name__ == "__main__":
	main()
