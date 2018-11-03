class Node():
	def __init__(self, value):
		self.left = None
		self.right = None
		self.parent = None
		self.val = value
		self.height = -1

class BinaryTree():
	def __init__(self):
		self.root = None
	
	def add(self, value):
		if (self.root == None):
			self.root = Node(value)
		else:
			self.addNode(value, self.root)

	def addNode(self, value, node):
		if (value < node.val):
			if (node.left != None):
				self.addNode(value, node.left)
			else:
				node.left = Node(value)
				node.left.parent = node

		else:
			if (node.right != None):
				self.addNode(value, node.right)
			else:
				node.right = Node(value)	
				node.right.parent = node
		
		self.rebalance(node)

	def height(self, node):
		if (node == None):
			return -1
		else:
			return node.height

	def update_height(self, node):
		node.height = max(self.height(node.left), self.height(node.right)) + 1

	def left_rotate(self, x):
		y = x.right
		y.parent = x.parent
		if (y.parent is None):
			self.root = y
		else:
			if (y.parent.left is x):
				y.parent.left = y
			elif (y.parent.right is x):
				y.parent.right = y
		x.right = y.left
		if x.right is not None:
			x.right.parent = x
		y.left = x
		x.parent = y
		self.update_height(x)
		self.update_height(y)

	def right_rotate(self, x):
		y = x.left
		y.parent = x.parent
		if (y.parent is None):
			self.root = y
		else:
			if (y.parent.left is x):
				y.parent.left = y
			elif (y.parent.right is x):
				y.parent.right = y
		x.left = y.right
		if x.left is not None:
			x.left.parent = x
		y.right = x
		x.parent = y
		self.update_height(x)
		self.update_height(y)

	def rebalance(self, node):
		while node is not None:
			self.update_height(node)
			if self.height(node.left) >= 2 + self.height(node.right):
				if self.height(node.left.left) >= self.height(node.left.right):
					self.right_rotate(node)
				else:
					self.left_rotate(node.left)
					self.right_rotate(node)
			elif self.height(node.right) >= 2 + self.height(node.left):
				if self.height(node.right.right) >= self.height(node.right.left):
					self.left_rotate(node)
				else:
					self.right_rotate(node.right)
					self.left_rotate(node)
			node = node.parent

	def printLevelOrder(self):
		h = self.height(self.root)
		for i in range(1, h + 3):
			self.printGivenLevel(self.root, i)
			print("\n")

	def printGivenLevel(self, node , level):
		if (node == None):
			return
		elif (level == 1):
			print ("%d" %(node.val)),
		else:
			self.printGivenLevel(node.left , level - 1)
			self.printGivenLevel(node.right , level - 1)
	
		

tree = BinaryTree()
tree.add(62)
tree.add(7)
tree.add(13)
tree.add(2)
tree.add(9)
tree.add(4)
tree.add(76)
tree.add(12)
tree.add(56)
tree.add(55)

tree.printLevelOrder()