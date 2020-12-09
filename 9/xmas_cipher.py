from itertools import combinations

#file shenanigans
file_puzzle_input = open("puzzle_input", 'r').read().splitlines()

#global variables
preamble_num = 25
nums = []
not_used = []
values = []

#function to find the item that doesn't belong for part 1
def find_not_sum():
	start = preamble_num
	beginning = 0
	for n in nums[preamble_num:]:
		exists = 0
		for p in combinations(nums[beginning:start], 2):
			if sum(p) == n:
				exists = 1	
		if exists == 0:
			not_used.append(n)
		beginning += 1
		start += 1

#parses input
def parse_input():
	for i,f in enumerate(file_puzzle_input):
		f = int(f)
		nums.append(f)

#finds list of numbers that are contiguous and add up to the number that doesn't belong
def find_contiguous():
	num = not_used[0]
	found = 0
	add = 0
	start = 0
	end = 0
	for i,n in enumerate(nums):
		start = i
		if n != num:
			add = n
			j = i + 1
			while j < len(nums) and found == 0:
				add += nums[j]
				j += 1
				if add == num:
					end = j
					found = 1
					get_values(i,j)
		else:
			continue

#gets answer to part 2
def encryption_weakness():
	values.sort()
	answer = values[0] + values[len(values) - 1]
	
	return answer

#creates list of numbers
def get_values(i,j):
	for n in nums[i:j]:
		values.append(n)

def main():
	parse_input()
	find_not_sum()
	print("the answer to part 1 is: " + str(not_used[0]))
	find_contiguous()
	print("the answer to part 2 is: " + str(encryption_weakness()))

if __name__ == "__main__":
	main()
