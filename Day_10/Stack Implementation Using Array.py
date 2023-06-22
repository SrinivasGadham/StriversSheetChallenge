from os import *
from sys import *
from collections import *
from math import *

# Stack class.
class Stack:
    
    def __init__(self, capacity: int):
        self.stack=[]
        self.capacity=capacity

    def push(self, num: int) -> None:
        if self.capacity!=len(self.stack):
            self.stack.append(num)
        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1


        
    def isEmpty(self) -> int:
        if len(self.stack)==0:
            return 1
        return 0

    
    def isFull(self) -> int:
        if self.capacity==len(self.stack):
            return 1
        return 0
        