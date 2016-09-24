#https://code.google.com/codejam/contest/351101/dashboard#s=p2
import os

class Input(object):
	def __init__(self, filename):
		super(Input, self).__init__()
		self.filename = filename
		self.__readInput()
		

	def __readInput(self):
		self.inputData = []
		try:
			with open(self.filename, "r") as fh:

				for linenum, line in enumerate(fh):
					if linenum == 0:
						self.cases = int(line)
					else:
						self.inputData.append(line.rstrip('\n'))
		except EnvironmentError:
			print "Something wrong in reading the file"

def getSeq(line):
	keynum = {"a":2, "b":2, "c":2, "d":3, "e":3, "f":3, "g":4, "h":4, "i":4, "j":5, "k":5, "l":5, "m":6, "n":6, "o":6, "p":7, "q":7, "r":7, "s":7, "t":8, "u":8, "v":8, "w":9, "x":9, "y":9, "z":9, ' ':0, '':-1}
	mapping = {"a":"2", "b":"22", "c":"222", "d":"3", "e":"33", "f":"333", "g":"4", "h":"44", "i":"444", "j":"5", "k":"55", "l":"555", "m":"6", "n":"66", "o":"666", "p":"7", "q":"77", "r":"777", "s":"7777", "t":"8", "u":"88", "v":"888", "w":"9", "x":"99", "y":"999", "z":"9999", ' ':"0"}
	prevchar = ''
	seq = ''
	for char in line:
		key = mapping.get(char, '')
		if keynum[char] == keynum[prevchar]:
			seq += ' ' + key
		else:
			seq += key
			prevchar = char

	return seq

if __name__ == "__main__":
	i = Input("C-large-practice.in")

	for casenum in range(1, i.cases+1):
		line = i.inputData[casenum-1]
		seq = getSeq(line)
		print "Case #%d: %s" %(casenum, seq)
