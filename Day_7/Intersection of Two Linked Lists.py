'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def findIntersection(firstHead, secondHead):
    first_len=0
    second_len=0
    ptr1=firstHead
    while ptr1:
        first_len+=1
        ptr1=ptr1.next
    ptr2=secondHead
    while ptr2:
        second_len+=1
        ptr2=ptr2.next
    ptr1=firstHead
    ptr2=secondHead
    if first_len<second_len:
        temp=second_len-first_len
        k=0
        while temp!=k:
            ptr2=ptr2.next
            k+=1
    elif first_len>second_len:
        temp=first_len-second_len
        k=0
        while temp!=k:
            ptr1=ptr1.next
            k+=1
    while ptr1 and ptr1!=ptr2:
        ptr1=ptr1.next
        ptr2=ptr2.next
    if ptr1==ptr2:
        return ptr2
    else:
        return None

    


    
	