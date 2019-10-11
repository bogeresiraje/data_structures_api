

def finobacci(length):
	''' Iterator finobacci function that will yield fino values. '''
	def fino(n):
		''' Function to find the nth value in the finobacci series. '''
		if n <= 1:
			return n
		else:
			return fino(n-1) + fino(n-2)

	for i in range(length):
		yield fino(i)

# Collect finobacci series in a list only when you want to access it.
# Or simply create a huge iterator object e.g ( finobacci(10000000000000) )
# In case there is further processing
# print(finobacci(1200000000000000000000))

# n = 100
# value = next((x for i,x in enumerate(finobacci(2000000000000)) if i == n), None)
# print(value)

print(list(finobacci(40)))