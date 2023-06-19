from math import *
from collections import *
from sys import *
from os import *

import sys
from sys import stdin

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def sortTwoLists(first, second):
    i=first
    j=second
    dummy=Node(-1)
    ptr=dummy
    while i and j:
        if i.data<=j.data:
            ptr.next=i
            ptr=i
            i=i.next
        else:
            ptr.next=j
            ptr=j
            j=j.next
    if i:
        ptr.next=i
    if j:
        ptr.next=j
    return dummy.next

    









def ll(arr):
    
    if len(arr)==0:
        return None
    
    head = Node(arr[0])
    last = head
    
    for data in arr[1:]:
        
        last.next = Node(data)
        last = last.next
        
    return head

def printll(head):
    
    while head:
        
        print(head.data, end=' ')
        
        head = head.next
        
    print(-1)

    

t = int(sys.stdin.readline().strip())

for i in range(t):
    
    arr1=list(map(int, sys.stdin.readline().strip().split(" ")))
    arr2=list(map(int, sys.stdin.readline().strip().split(" ")))
    
    l1 = ll(arr1[:-1])
    l2 = ll(arr2[:-1])
    
    l = sortTwoLists(l1, l2)
    
    printll(l)

