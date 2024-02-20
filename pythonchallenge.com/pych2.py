import string
file="chars1.txt"

alpha = string.ascii_lowercase
chars = []
with open(file) as f:
	for line in f:
		for char in line:
			if char.lower() in alpha:
				chars.append(char)

print("".join(chars))
