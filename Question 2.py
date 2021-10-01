

# Node class
class Node:
	
	# Function to initialize the node object
	def __init__(self, data):

		self.data = data
		self.next = None
	
# Linked List Class
class LinkedList:

	# Function to initialize the LinkedList class.
	def __init__(self):

		# Initialize head as None
		self.head = None

	# This function insert a new node at the
	# beginning of the linked list
	def push(self, new_data):
	
		# Create a new Node
		new_node = Node(new_data)

		# Make next of new Node as head
		new_node.next = self.head

		# Move the head to point to new Node
		self.head = new_node
		
	# Method to print the linked list
	def printList(self):

		# Object to iterate
		# the list
		ptr = self.head

		# Loop to iterate list
		while(ptr != None):
			print(ptr.data, '->', end = '')

			# Moving the iterating object
			# to next node
			ptr = ptr.next
			
		print()

# Function to reverse the linked
# list and return its length
def reverse(head_ref):

	# Initialising prev and current
	# at None and starting node
	# respectively.
	prev = None
	current = head_ref.head

	Len = 0

	# Loop to reverse the link
	# of each node in the list
	while(current != None):
		Len += 1
		Next = current.next
		current.next = prev
		prev = current
		current = Next

	# Assigning new starting object
	# to main head object.
	head_ref.head = prev

	# Returning the length of
	# linked list.
	return Len

# Function to define an empty
# linked list of given size and
# each element as zero.
def make_empty_list(size):
	
	head = LinkedList()
	
	while(size):
		head.push(0)
		size -= 1

	# Returns the head object.
	return head

# Multiply contents of two linked
# list store it in other list and
# return its head.
def multiplyTwoLists(first, second):

	# Reverse the list to multiply from
	# end m and n lengths of linked list
	# to make and empty list
	m = reverse(first)
	n = reverse(second)

	# Make a list that will contain the
	# result of multiplication.
	# m+n+1 can be max size of the list.
	result = make_empty_list(m + n + 1)

	# Objects for traverse linked list
	# and also to reverse them after.
	second_ptr = second.head
	result_ptr1 = result.head

	# Multiply each node of second
	# list with first.
	while(second_ptr != None):
		carry = 0

		# Each time we start from next
		# node from which we started last
		# time.
		result_ptr2 = result_ptr1
		first_ptr = first.head

		while(first_ptr != None):
			
			# Multiply a first list's digit
			# with a current second list's digit.
			mul = ((first_ptr.data) *
				(second_ptr.data) + carry)

			# Assign the product to corresponding
			# node of result.
			result_ptr2.data += mul % 10

			# Now resultant node itself can have
			# more then one digit.
			carry = ((mul // 10) +
					(result_ptr2.data // 10))
			result_ptr2.data = result_ptr2.data % 10

			first_ptr = first_ptr.next
			result_ptr2 = result_ptr2.next

		# If carry is remaining from
		# last multiplication
		if(carry > 0):
			result_ptr2.data += carry

		result_ptr1 = result_ptr1.next
		second_ptr = second_ptr.next

	# Reverse the result_list as it
	# was populated from last node
	reverse(result)
	reverse(first)
	reverse(second)

	# Remove starting nodes
	# containing zeroes.
	start = result.head
	while(start.data == 0):
		result.head = start.next
		start = start.next

	# Return the resultant multiplicated
	# linked list.
	return result

# Driver code
if __name__=='__main__':

	first = LinkedList()
	second = LinkedList()

	# Pushing elements at start of
	# first linked list.
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)

	# Printing first linked list
	print("First list is: ", end = '')
	first.printList()

	# Pushing elements at start of
	# second linked list.
	
	second.push(9)
	second.push(8)
	second.push(7)
	second.push(6)
	second.push(5)
	second.push(4)
	second.push(3)
	second.push(2)
	second.push(1)
	
	

	# Printing second linked list.
	print("Second List is: ", end = '')
	second.printList()

	# Multiply two linked list and
	# print the result.
	result = multiplyTwoLists(first, second)
	print("Resultant list is: ", end = '')
	result.printList()
