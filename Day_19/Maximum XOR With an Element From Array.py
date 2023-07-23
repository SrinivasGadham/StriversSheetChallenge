def maxXorQueries(nums, queries):
	
	nums.sort()
	queries = sorted((m, x, i) for i, (x, m) in enumerate(queries))
	ans = [-1]*len(queries)
	
	
	
	trie = {}
	k = 0
	for m, x, i in queries: 
		
		while k < len(nums) and nums[k] <= m: 
			def add_num(x):
				cur = trie
				for bit in format(x, '032b'):
					if bit not in cur:
						cur[bit] = {}
					cur = cur[bit]
				cur['value'] = x
				return

			add_num(nums[k])
			k += 1

		
		if trie: 
			def best_match(x):
				cur = trie
				for bit in format(x, '032b'):
					rev = '0' if bit == '1' else '1'
					if rev in cur:
						cur = cur[rev]
					else:
						cur = cur[bit]
				return cur['value']

			ans[i] = x ^ best_match(x)

	return ans 