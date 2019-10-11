
class DoublyLinkedBase:
	''' A base class providing a doubly linked lis representation. '''

	class Node:
		''' Nonweight non-public class for storing a doubly linked node. '''
		__slots__ = '_element', '_prev', '_next'	# Streamline memory

		def __init__(self, element, prev, next):	# Initialize Node's fields
			self._element = element 	# User element
			self._prev = prev 	# Previous node reference
			self._next = next 	# Next node reference

	def __init__(self):
		'''Create an empty list. '''
		self._header = self.Node(None, None, None)
		self._trailer = self.Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0

	def __len__(self):
		''' return number of elements of the list. '''
		return self._size

	def is_empty(self):
		''' Return True if list is empty. '''
		return self._size == 0

	def insert_between(self, e, predecessor, successor):
		''' Add element between two existing nodes and return its element. '''
		newest = self.Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1
		return newest

	def delete_node(self, node):
		''' Delete nonsentinal node from the list and return its element. '''
		predecessor = node._prev
		successor = node._next
		predecessor._next = successor
		successor._prev = predecessor
		self._size -= 1
		element = node._element 	# Record deleted element
		node._prev = node._next = node._element = None 	# Deprecate node
		return element