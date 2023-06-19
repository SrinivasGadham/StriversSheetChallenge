'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def removeKthNode(head, k):
    temp=1
    slow=head
    fast=head
    while k!=temp:
        fast=fast.next
        temp+=1
    while fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next
    if slow==head:
        return head.next
    prev.next=slow.next
    return head

   