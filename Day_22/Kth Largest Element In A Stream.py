def __init__(self, k, nums):
	"""
	:type k: int
	:type nums: List[int]
	"""
	self.arr = sorted(nums)
	self.k = k

def add(self, val):
	"""
	:type val: int
	:rtype: int
	"""
	# self.arr = sorted(self.arr + [val])[-self.k:]
	bisect.insort(self.arr, val)
	return self.arr[-self.k]