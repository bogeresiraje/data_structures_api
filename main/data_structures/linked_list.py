
from main.data_structures.doubly_linked_base import DoublyLinkedBase

class PositionalList(DoublyLinkedBase):
 	'''A sequential container of elements allowing positional access.'''
 	#-------------------------- nested Position class -------------------------
 	class Position:
 		'''An abstraction representing the location of a single element.'''
 		def __init__ (self, container, node):
 			''' Constructor should not be invoked by user. ''' 
 			self._container = container
 			self._node = node

 		def element(self):
 			'''Return the element stored at this Position. '''
 			return self._node._element

 		def __eq__(self, other):
 			'''Return True if other is a Position representing the same location.'''
 			return type(other) is type(self) and other._node is self._node

 		def __ne__(self, other): 
 			'''Return True if other does not represent the same location.'''
 			return not (self == other)	# opposite of eq


 	def __init__(self):
 		super(PositionalList, self).__init__()

 	#------------------------------- utility method ------------------------------
 	def validate(self, p):
 		'''Return position s node, or raise appropriate error if invalid.'''
 		if not isinstance(p, self.Position):
 			raise TypeError('p must be proper Position type')
 		if p._container is not self:
 			raise ValueError('p does not belong to this container')
 		if p._node._next is None:
 			# convention for deprecated nodes 33 
 			raise ValueError('p is no longer valid')
 		return p._node

 	# Utility method
 	def make_position(self, node):
 		''' Return position instance for a given node. '''
 		if node is self._header or node is self._trailer:
 			return None
 		else:
 			return self.Position(self, node)

 	#------------------------------- accessor methods ------------------------------
 	def first(self):
 		''' Return the first position in the list ( None if empty ). '''
 		return self.make_position(self._header._next)

 	def last(self):
 		''' Return last position in the list ( None if empty ). '''
 		return self.make_position(self._trailer._prev)

 	def before(self, p):
 		'''Return the Position just before Position p (or None if p is ﬁrst). '''
 		node = self.validate(p)
 		return self.make_position(node._prev)

 	def after(self, p):
 		''' Return the Position just after Position p (or None if p is last). '''
 		node = self.validate(p)
 		return self.make_position(node._next)

 	def __iter__(self):
 		''' Generate a forward iteration of elements of the list. '''
 		cursor = self.first()
 		while cursor is not None:
 			yield cursor.element()
 			cursor = self.after(cursor)

 	def insert_between(self, e, predecessor, successor):
 		''' Add element between existing node and return new Position. '''
 		node = super().insert_between(e, predecessor, successor)
 		return self.make_position(node)

 	def add_first(self, e):
 		''' Insert element at the front of the list and return new Position. '''
 		return self.insert_between(e, self._header, self._header._next)

 	def add_last(self, e):
 		''' Add element at the back of the element and return new position. '''
 		return self.insert_between(e, self._trailer._prev, self._trailer)

 	def add_before(self, p, e):
 		''' Add element e before position p, and return new Position. '''
 		original = self.validate(p)
 		return self.insert_between(e, original._prev, original)

 	def add_after(self, p, e):
 		''' Insert element e into the list, and return new Position. '''
 		original = self.validate(p)
 		return self.insert_between(e, original, original._next)

 	def delete(self, p):
 		''' Remove and return the element at position p. '''
 		original = self.validate(p)
 		return self.delete_node(original)

 	def delete_first(self, p):
 		''' Remove and return the element at position p. '''
 		original = self.validate(p)
 		return self.delete_node(original)