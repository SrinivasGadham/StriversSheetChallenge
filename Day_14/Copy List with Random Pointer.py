from math import *

from collections import *

from sys import *

from os import *

 

class LinkedListNode:

    def __init__(self,data):

        self.data = data

        self.next = None

        self.random = None

        

 

def cloneRandomList(head):

    # Your code goes here.

    if head is None :

        return None

    temp=head

    while temp:

        new_node = LinkedListNode(temp.data)

        new_node.next=temp.next

        temp.next = new_node

        temp=temp.next.next;

    itr=head

    while itr:

        if itr.random!=None:

            itr.next.random=itr.random.next

        itr=itr.next.next 

    dummy = LinkedListNode(0)

    itr=head

    temp=dummy

    while itr:

        fast = itr.next.next

        temp.next=itr.next

        itr.next=fast

        temp=temp.next

        itr=fast

 

    return dummy.next