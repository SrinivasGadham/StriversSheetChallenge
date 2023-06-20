class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


def rotate(head: Node, k: int) -> Node:
    if not head or not head.next:
        return head
    link_len=0
    ptr=head
    
    while ptr:
        ptr=ptr.next
        link_len+=1
    k=k%link_len
    temp=1
    ptr=head
    if k==link_len or k==0:
        return head
    while temp!=(link_len-k):
        ptr=ptr.next
        temp+=1
    # print(ptr.data)
    last_node=ptr
    first_node=ptr.next
    ptr=head
    
    while ptr.next:
        ptr=ptr.next
    ptr.next=head
    head=first_node
    last_node.next=None
    return head
    

    


    
