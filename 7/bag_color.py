import re

file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
bags = []
contain_gold = []
gold_num = 0

#define bag objects
class bag():
	def __init__(self):
		self.bag_contents = {}
		self.num_contents = 0
		self.color = ""
		self.contains_gold = 0
		self.can_contain_gold = 0

#find objects that already contain gold
def contains_gold():
	for i in range(len(bags)):
		if "shiny gold" in bags[i].bag_contents:
			bags[i].contains_gold = 1
			bags[i].can_contain_gold = 1
			contain_gold.append(bags[i])

#find objects that contain objects that already contain gold
def find_more_gold():
	for j in contain_gold:
		for k in bags:
			if j.color in k.bag_contents:
				k.can_contain_gold = 1
				contain_gold.append(k)			

#basic search to iterate through list of bag objects
def search_bags(search_term):
	index = 0
	for i,b in enumerate(bags):
		if b.color == search_term:
			index = i
			break
		else:
			continue
	return index

#figure out how many bags are inside a given type of bag
def shiny(i, search_term):
	global gold_num
	index = search_bags(search_term)
	i = int(i)
	for k in bags[index].bag_contents:
		num = int(bags[index].bag_contents[k])
		gold_num = gold_num + (num * i)
		parent = num * i
		shiny(parent, k)


def main():
	gold = 0

	#clearly i need to work on reading from files & string manipulation
	for line in file_puzzle_input:
		items = re.split(r'((\d+).*)', line)
		new_bag = bag()
		bags_inside = []
		color = items[0]
		color = color.split(' ')
		final_color = color[0] + ' ' + color[1]
		new_bag.color = final_color

		if len(items) > 1:
			inside = items[1]
			bags_inside = inside.split(',')
		for b in bags_inside:
			new = b.strip()
			new_item = new.split(' ')
			num = new_item[0]
			description = new_item[1] + ' ' + new_item[2]
			new_bag.bag_contents.update({description: num})
		bags.append(new_bag)

#part 1
	contains_gold()
	find_more_gold()
	for b in bags:
		if b.can_contain_gold == 1:
			gold += 1
	print("the answer to part one is " + str(gold))

#part 2
	shiny(1, "shiny gold")
	print("the answer to part two is " + str(gold_num))

if __name__ == "__main__":
	main()	
