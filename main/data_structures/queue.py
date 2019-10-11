
class ArrayQueue:
	'''
		FIFO queue implementation using Python list as underlying storage
	'''
	DEFAULT_CAPACITY = 10	# Moderate capacity for all queues.

	def __init__(self):
		''' Create an empty queue. '''
		self._data = [None] * self.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		''' Return the number of elements in the queue. '''
		return self._size

	def is_empty(self):
		''' Return True if queue is empty. '''
		return self._size == 0

	def first(self):
		''' Return ( but do not remove ) element at the front of the queue. '''
		return self._data[self._front]

	def dequeue(self):
		''' Remove and return the first element of the queue. '''
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		return answer

	def enqueue(self, e):
		''' Add an element at the back of the queue. '''
		if self._size == len(self._data):
			self.resize(2 * len(self._data))
		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = e
		self._size += 1


	def resize(self, cap):
		''' Resize to a new list >= len(self). '''
		old = self._data	# Keep data of existing list.
		self._data = [None] * cap 	# Allocate list with new capacity.
		walk = self._front
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1 + walk) % len(old)
		self._front = 0

	def get_elements(self):
		''' Returns all elements in the queue. '''
		for e in self._data:
			if e is not None:
				yield e

	def list_size(self):
		''' Checks the size of the list. '''
		return len(self._data)

	def is_full(self):
		''' Checks whether the queue is full. '''
		return self._size == len(self._data)
