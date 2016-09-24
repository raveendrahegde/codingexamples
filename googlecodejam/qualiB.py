#https://code.google.com/codejam/contest/351101/dashboard#s=p1
import os

class Input(object):
	"""docstring for Input"""
	def __init__(self, filename):
		super(Input, self).__init__()
		self.filename = filename
		self.__readInput()
		

	def __readInput(self):
		"TODO:Convert to a generator"
		self.inputData = []
		try:
			with open(self.filename, "r") as fh:

				for linenum, line in enumerate(fh):
					if linenum == 0:
						self.cases = int(line)
					else:
						self.inputData.append(line)
		except EnvironmentError:
			print "Something wrong in reading the file"

def lineReverse(line):
	words = line.split()
	words.reverse()
	return " ".join(words)

if __name__ == "__main__":
	i = Input("B-large-practice.in")

	for casenum in range(1, i.cases+1):
		line = i.inputData[casenum-1]
		reversline = lineReverse(line)
		print "Case #%d: %s" %(casenum, reversline)
