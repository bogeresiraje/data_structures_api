
class PList(object):
	def __init__(self):
		self.type = 'linked_list'
		self.data = []

	def get_elements(self):
		return self.data

	def add_first(self, e):
		self.data.insert(0, e)

	def add_last(self, e):
		self.data.insert(len(self.data), e)

	def add_after(self, index, e):
		self.data.insert(index+1, e)

	def add_before(self, index, e):
		self.data.insert(index-1, e)

	def delete_first(self):
		self.data.pop(0)

	def delete_last(self):
		self.data.pop(-1)

	def delete_after(self, index):
		self.data.pop(index+1)

	def delete_before(self, index):
		self.data.pop(index-1)
