# augest22
my first repository

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None

	def add_child(self, child):
		child.parent = self
		self.children.append(child)


def build_product_tree():
	root = TreeNode('Electronics')
	laptop = TreeNode('Laptop')
	laptop.add_child(TreeNode('Macbook'))
	laptop.add_child(TreeNode('Lenovo'))
	laptop.add_child(TreeNode('Asus'))

	cellphone = TreeNode('Cellphone')
	cellphone.add_child(TreeNode('Iphone'))
	cellphone.add_child(TreeNode('Samsung'))
	cellphone.add_child(TreeNode('Redmi'))

	tv = TreeNode('Tv')
	tv.add_child(TreeNode('Lg'))
	tv.add_child(TreeNode('Sharp'))

	root.add_child(laptop)
	root.add_child(cellphone)
	root.add_child(tv)

	return root


if __name__ == '__main__':
	root = build_product_tree()
	pass

