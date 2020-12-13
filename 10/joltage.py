file_puzzle_input = open("puzzle_input", 'r').read().splitlines()
adapter_joltage = []

def parse():
	for f in file_puzzle_input:
		adapter_joltage.append(int(f))

def part_1():
	diff_one = 1
	diff_three = 1
	for i,a in enumerate(adapter_joltage):
		if a - adapter_joltage[i - 1] == 1:
			diff_one += 1
		elif a - adapter_joltage[i - 1] == 3:
			diff_three += 1
		else:
			continue
	return diff_one * diff_three 

class num_obj():
	def __init__(self):
		self.num = 0
		self.paths = 0

def part_2():
	#add beginning and end
	adapter_joltage.append(0)
	adapter_joltage.sort()
	adapter_joltage.append(adapter_joltage[- 1] + 3)

	#declare variables
	nums = []
	total = 0

	#create objects to track paths
	for a in adapter_joltage:
		new_num = num_obj()
		new_num.num = a
		nums.append(new_num)

	#find paths
	nums[0].paths = 1
	j = 0
	length = len(nums)
	while j < length:
		i = j + 1
		while i < length:
			if (nums[j].num + 1) == nums[i].num:
				nums[i].paths += nums[j].paths
			elif (nums[j].num + 2) == nums[i].num:
				nums[i].paths += nums[j].paths
			elif (nums[j].num + 3) == nums[i].num:
				nums[i].paths += nums[j].paths
			i += 1
		j += 1
	total = nums[-1].paths
	return total

def main():
	parse()
	adapter_joltage.sort()
	print("the answer for part 1 is: " + str(part_1()))
	print("the answer for part 2 is: " + str(part_2()))

if __name__ == "__main__":
	main()
