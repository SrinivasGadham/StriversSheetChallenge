
from collections import deque
def slidingWindowMaximum(nums:list, k:int):
	d=deque()
	i=0
	j=0
	res=[]
	while(j<len(nums)):
		while len(d)>0 and d[-1]<nums[j]:
			d.pop()
		d.append(nums[j])
		if j-i+1<k:
			j+=1
		elif j-i+1==k:
			res.append(d[0])
			if d[0]==nums[i]:
				d.popleft()
			i+=1
			j+=1
	return res
	




	