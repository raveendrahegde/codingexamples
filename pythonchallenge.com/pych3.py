import string
file="pych3.txt"

def extract(data, start, end):
	started = False
	ended = False
	needed = []
	for line in data:
		if start in line:
			started = True
			continue #exclude the start line
		if end in line:
			ended = True

		if started and not ended:
			needed.append(line.rstrip())

	return needed

with open(file) as f:
	data = f.readlines()
	datablock = extract(data, '<!--', '-->')
	datablock = "".join(datablock)

	interesting = []

	for index, char in enumerate(datablock):
		if char.isupper():
			continue

		if index > 2 and index < len(datablock) - 3:
			left = datablock[index-3: index]
			right = datablock[index+1: index+4]

			if index > 4:
				lleft = datablock[index-4]
			if index + 4 <= len(datablock) - 1:
				rright = datablock[index+4]

			if left.isupper() and lleft.islower() and right.isupper() and rright.islower():
				interesting.append(char)

	print "".join(interesting)





