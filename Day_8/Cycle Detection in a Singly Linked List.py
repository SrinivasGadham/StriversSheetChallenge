'''
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''

def detectCycle(head) :
    if head==None or head.next==None:
        return False
    slow=head
    fast=head
    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
        if slow==head:
            return True
    return False
    