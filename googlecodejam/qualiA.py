#https://code.google.com/codejam/contest/351101/dashboard#s=p0

class Input(object):
	"""docstring for Input"""
	def __init__(self, filename):
		super(Input, self).__init__()
		self.filename = filename
		self.__readInput()
		

	def __readInput(self):
		self.inputData = []
		fh = open(self.filename, "r")
		self.handle = fh

		for linenum, line in enumerate(fh):
			if linenum == 0:
				self.cases = int(line)
			else:
				self.inputData.append(line.rstrip())


def calc(credit, items, prices):
	for num in range(items):
		firstitem = prices[num]
		for secnum, seconditem in enumerate(prices):
			if secnum == num:
				continue
			else:
				if firstitem + seconditem == credit:
					return num+1, secnum+1

if __name__ == "__main__":
	i = Input("A-large-practice.in")
	positions = []
	# print i.inputData
	
	for casenum in range(1, i.cases+1):
		end = casenum*3
		start = end - 3
		values = i.inputData[start:end]
		credit = int(values[0])
		nitems = int(values[1])
		prices = values[-1].split()
		prices = [int(x) for x in prices]
		pos = calc(credit, nitems, prices)
		positions.append(pos)

	for case, pos in enumerate(positions):
		print 'Case #%d: %d %d' %(case+1, pos[0], pos[1])




	