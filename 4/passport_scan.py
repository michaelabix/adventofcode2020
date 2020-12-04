import re

#file shenanigans
file_puzzle_input = open("puzzle_input", 'r').read().splitlines()

#declare variables
num = 0

#declare empty arrays
passports = []
potentially_valid = []
valid = []
pp_valid = 0
np_valid = 0

#condense fields-per-passport to one line
passports.append("")
for line in file_puzzle_input:
	if re.match('^$',line):
		num += 1
		passports.append("")
	else:
		passports[num] = passports[num] + line.strip() + ' '

#eliminate items that don't have enough fields to be valid
for item in passports:
	if re.match('^(\S+\s){7,8}$', item):
		potentially_valid.append(item)

#part 1
#identify that the correct fields exist per potentially valid passport
for item in potentially_valid:
	if re.match('^.*byr:.+$', item):
		if re.match('^.*iyr:.+$', item):
			if re.match('^.*eyr:.+$', item):
				if re.match('^.*hgt:.+$', item):
					if re.match('^.*hcl:.+$', item):
						if re.match('^.*ecl:.+$', item):
							if re.match('^.*pid:.+$',item):
								if re.match('^.*cid:.+$', item):
									valid.append(item)
									pp_valid += 1
								else:
									valid.append(item)
									np_valid += 1

print "the total number of valid passports and north pole ids for part 1 is " + str(pp_valid + np_valid)	

#part 2

very_valid = []
vv_valid = 0

for v in valid:
	byr = 0
	iyr = 0
	eyr = 0
	hgt = 0
	hcl = 0
	ecl = 0
	pid = 0
	#parse lines
	chunks = v.split(' ')
	chunks.sort()
	del chunks[0]
	if len(chunks) == 8:
		del chunks[1]
	for n in chunks:
		smaller_chunks = n.split(':')
		key = smaller_chunks[0]
		desc = smaller_chunks[1]
		if key == "byr" and (int(desc) >= 1920 and int(desc) <= 2002):
			byr = 1

		if key == "iyr" and (int(desc) >= 2010 and int(desc) <= 2020):
			iyr = 1

		if key == "eyr" and (int(desc) >= 2020 and int(desc) <= 2030):
			eyr = 1

		if key == "hgt":
			if re.match('^.*cm.*$', desc):
				desc = desc[:-2]
				if int(desc) >= 150 and int(desc) <= 193:
					hgt = 1
			elif re.match('^.*in.*$', desc):
				desc = desc[:-2]
				if int(desc) >= 59 and int(desc) <= 76:
					hgt = 1
			else:
				break
	
		if key == "hcl" and re.match('^#[0-9,a-f]{6}', desc):
			hcl = 1
	
		if key == "ecl" and re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', desc):
			ecl = 1
	
		if key == "pid" and re.match('^\d{9}$', desc):
			pid = 1
	
	if byr == 1 and iyr == 1 and eyr == 1 and hgt == 1 and hcl == 1 and ecl == 1 and pid == 1:
		vv_valid += 1
		very_valid.append(v)

print "the total number of valid passports and north pole ids for part 2 is " +  str(vv_valid)	
