#https://code.google.com/codejam/contest/351101/dashboard#s=p2
import math
import numpy

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

def distances(line):
	l = line.split(" ")
	l = [int(p) for p in l]
	t = [(l[0], l[1]), (l[2], l[3]), (l[4], l[5])]

	dist12 = math.sqrt(math.pow((t[1][0]-t[0][0]), 2) + math.pow((t[1][1]-t[0][1]), 2))
	dist23 = math.sqrt(math.pow((t[2][0]-t[1][0]), 2) + math.pow((t[2][1]-t[1][1]), 2))
	dist13 = math.sqrt(math.pow((t[2][0]-t[0][0]), 2) + math.pow((t[2][1]-t[0][1]), 2))

	return dist12, dist23, dist13

def isTriangle(dist12, dist23, dist13):
	# print dist12, dist23, dist13
	if dist13 == (dist12 + dist23):
		return False
	elif dist23 == (dist13 + dist12):
		return False
	elif dist12 == (dist13 + dist23):
		return False
	else:
		return True

def get_ltype(a, b, c):
	if a != b and a != c and b != c:
		return 'scalene'
	else:
		return 'isosceles'

def get_atype(a, b, c):
	sides = [a, b, c]
	sides.sort(reverse=True)

	# print math.acos(1.0)
	result = (math.pow(sides[1], 2) + math.pow(sides[2], 2) - math.pow(sides[0], 2))/(2*sides[1]*sides[2])
	# print "RESULT"
	# print "%.10f"%result

	largest_angle_rad = math.acos(result)
	largest_angle = math.degrees(largest_angle_rad)
	
	print largest_angle
	if largest_angle == 90:
		return 'right'
	elif largest_angle > 90:
		return 'obtuse'
	else:
		return 'acute'

if __name__ == "__main__":
	i = Input("probA-large-practice.in")

	for casenum in range(1, i.cases+1):
		line = i.inputData[casenum-1]
		dist12, dist23, dist13 = distances(line)
		tri = isTriangle(dist12, dist23, dist13)
		if tri:
			ltype = get_ltype(dist12, dist23, dist13)
			atype = get_atype(dist12, dist23, dist13)
			print "Case #%d: %s %s triangle" %(casenum, ltype, atype)
		else:
			pass
			print "Case #%d: %s" %(casenum, "not a triangle")
