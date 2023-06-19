'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def firstNode(head):
    if not head or not head.next:
        return None
    slow=head
    fast=head
    flag=0
    while slow and fast and fast.next:
        # print("hii")
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            flag=1
            break
        if slow==head:
            return slow
    # print(flag)
    if flag==1:
        count=0
        slow=head
        while fast!=slow:
            slow=slow.next
            fast=fast.next
            count+=1
        return slow
    else:
        return None


    