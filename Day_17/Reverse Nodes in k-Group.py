from math import *
from collections import *
from sys import *
from os import *


class Node:
    def __init__(self, data):
       	self.data = data
        # self.next = None


def helper(head, index, n, block):
    
    
    if head is None or index >= n:
        return head
    count = 0
    current_el = head
    prev_el = None
    next_el = None
    while current_el and count < block[index]:
        next_el = current_el.next
        
        current_el.next = prev_el
        
        
        
        prev_el = current_el
        current_el = next_el
        count += 1
    
    
    
    if next_el:
        index += 1
        
        
        while index < n and block[index] == 0:
            index += 1
        
        head.next = helper(next_el, index, n, block)
    
    return prev_el


def getListAfterReverseOperation(head, n, block):
    
    
    if n == 1 and block[0] <= 1:
        return head
    return helper(head, 0, n, block)