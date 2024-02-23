sentence=''
details={}

while sentence == '':
	sentence=raw_input("Plese enter sentence:")

words=sentence.split()

for word in words:
	if word in details:
		details[word] += 1
	else:
		details[word] = 1

for key, val in details.iteritems():
	print "Word  " +  key + " " + str(val) + " times"