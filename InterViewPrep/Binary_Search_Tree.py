class Node(object):
	def __init__(self,val):
		self.data=val
		self.left=None
		self.right=None

class BST(object):
	def insert(self, root, node):
		if root.left is None and node.data < root.data:
			root.left = node
			return
		if root.right is None and node.data >= root.data:
			root.right = node
			return
		if node.data < root.data:
			self.insert(root.left, node)
		if node.data >= root.data: 
			self.insert(root.right, node)

	def in_order_print(self, root):
		if root.left is None and root.right is None:
			print root.data
			return
		self.in_order_print(root.left)
		print root.data
		self.in_order_print(root.right)

	def pre_order_print(self, root):
		if root.left is None and root.right is None:
			print root.data
			return
		print root.data
		self.pre_order_print(root.left)
		self.pre_order_print(root.right)

	def post_order_print(self, root):
		if root.left is None and root.right is None:
			print root.data
			return
		self.pre_order_print(root.left)
		self.pre_order_print(root.right)
		print root.data

	def level_order_print(self, root, level=0):
		currentlevel=0
		if currentlevel == level:
			print root.data
			return
		if root.left is not None:
			self.level_order_print(root.left, level-1)
		if root.right is not None:
			self.level_order_print(root.right, level-1)


bst=BST()
r=Node(45)

bst.insert(r,Node(46))
bst.insert(r,Node(73))
bst.insert(r,Node(55))
bst.insert(r,Node(11))
bst.insert(r,Node(99))
bst.insert(r,Node(45))

print "\nIn order\n"
bst.in_order_print(r)
print "\nPre order\n"
bst.pre_order_print(r)
print "\nPost order\n"
bst.post_order_print(r)
for l in range(5):
	print "\nLevel order for level " + str(l)
	bst.level_order_print(r, l)







	