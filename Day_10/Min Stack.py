from os import *
from sys import *
from collections import *
from math import *

# Implement class for minStack.
class minStack:

	# Write your code here.
			
    # Constructor
    def __init__(self):
        self.min1=float('inf')
        self.min2=float('inf')
        self.stack=[]
    
    # Function to add another element equal to num at the top of stack.
    def push(self, num: int) -> None:
        self.stack.append(num)
        temp=self.min1
        if len(self.stack)==1:
            self.min1=min(self.min1,num)
        elif len(self.stack)>1:
            self.min2=temp
    
    # Function to remove the top element of the stack.
    def pop(self) -> int:
        if len(self.stack)==0:
            return -1
        if len(self.stack)>=2:
            self.min1=self.min2
            self.min2=float('inf')
        
        return self.stack.pop()
    
    # Function to return the top element of stack if it is present. Otherwise return -1.
    def top(self) -> int:
        if len(self.stack)==0:
            return -1
        return self.stack[-1]
        
    # Function to return del st.Min[:]inimum element of stack if it is present. Otherwise return -1.
    def getMin(self) -> int:
        if len(self.stack)==0:
            return -1
        return self.min1

        