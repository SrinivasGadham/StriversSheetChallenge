class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.


def merge(down,right):
    if(down == None):
        return right
    if(right == None):
        return down
    ans = Node(-1)
    temp = ans
    while(down!=None and right!=None):
        if(down.data<right.data):
            temp.child = down
            temp = down
            down = down.child
        else:
            temp.child = right
            temp = right
            right = right.child
            
    #if right part is none and elements left in leftpart
    while(down!=None):
        temp.child = down
        temp =down
        down = down.child
    while(right!=None):
        temp.child = right
        temp = right
        right = right.child
    ans = ans.child
    return ans

def flattenLinkedList(head):
    if(head == None or head.next == None):
        return head
    down = head
    right = down.next
    down.next = None
    right = flattenLinkedList(right)
    
    result = merge(down,right)
    return result
    
