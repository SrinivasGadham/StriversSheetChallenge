from typing import *

class TrieNode:
    def __init__(self):
        self.children = dict()                       
        self.val = 0   

class Trie:
    def __init__(self, n):
        self.root = TrieNode()                    
        self.n = n   
        
    def add_num(self, num):
        node = self.root 
        for shift in range(self.n, -1, -1):        
            val = 1 if num & (1 << shift) else 0   
            if val not in node.children:
                node.children[val] = TrieNode()
            node = node.children[val]
        node.val = num
        
def maximumXor(nums: List[int]) -> int:
    
    max_len = len(bin(max(nums))) - 2 
    trie = Trie(max_len)
    for num in nums: 
        trie.add_num(num)        
        
    ans = 0
    
    for num in nums:   
        node = trie.root 
        for shift in range(max_len, -1, -1):
            val = 1 if num & (1 << shift) else 0  
            
            node = node.children[1-val] if 1-val in node.children else node.children[val] 
        
        ans = max(ans, num ^ node.val)  
    
    return ans    