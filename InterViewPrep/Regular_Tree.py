class Node(object):
	def __init__(self, data):
		self.data = data
		self.children =[]

	def add_child(self, obj):
		self.children.append(obj)


if __name__ == '__main__':
	a=Node(5)
	b=Node(3)
	c=Node(15)
	c.add_child(Node(55))
	b.add_child(Node(24))
	a.add_child(b)
	a.add_child(Node(6))
	a.add_child(c)

	def print_nodes(node):
		print node.data
		for child in node.children:
			if child.children:
				print_nodes(child)
			else:
				print child.data
	def print_nodesof_level(node, level=0):
		currentlevel=0
		if level == currentlevel:
			print node.data
			return
		currentlevel +=1
		for child in node.children:
			if  currentlevel == level:
				print child.data
			else:
				if child.children:
					print_nodesof_level(child, level-1)


	print "All nodes"
	print_nodes(a)
	levels = [0, 1,2,3]
	for level in levels:
		print "\nNodes of level " + str(level)
		print_nodesof_level(a, level)
			
	