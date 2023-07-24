

class Node:
	def __init__(self, val):
		self.right = None
		self.data = val
		self.left = None


prev = None

def BinaryTree2DoubleLinkedList(root):
	
	
	if root is None:
		return root
			
	
	head = BinaryTree2DoubleLinkedList(root.left);
	
	
	
	global prev
	
	
	
	if prev is None :
		head = root
		
	else:
		root.left = prev
		prev.right = root
	
	
	prev = root;
	
	
	BinaryTree2DoubleLinkedList(root.right);
	
	return head

def print_dll(head):
	
	
	
	while head is not None:
		print(head.data, end=" ")
		head = head.right





if __name__ == '__main__':
	root = Node(10)
	root.left = Node(12)
	root.right = Node(15)
	root.left.left = Node(25)
	root.left.right = Node(30)
	root.right.left = Node(36)
	
	head = BinaryTree2DoubleLinkedList(root)
	
	
	print_dll(head)
	

