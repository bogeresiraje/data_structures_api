
class ArrayStack:
	'''
		Implementing LIFO stack using a Python list as an underlying storage
	'''
	def __init__(self):
		self._data = []

	def __len__(self):
		'''
			Return number of elemnts in the stack
		'''
		return len(self._data)

	def is_empty(self):
		'''
			Return True if stack is empty
		'''
		return len(self._data) == 0

	def push(self, e):
		''' Add element to the top of the stack. '''
		self._data.append(e)

	def top(self):
		''' Return ( but do not remove ) element at the top of the stack. '''
		return self._data[-1]

	def pop(self):
		''' Remove and return element at the top of the stack. '''
		return self._data.pop()

	def elements(self):
		''' Returns all elements of the stack. '''
		return self._data