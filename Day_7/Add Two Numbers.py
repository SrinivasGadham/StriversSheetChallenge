class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    carry=0
    dummy=Node(-1)
    num1=head1
    num2=head2
    ptr=dummy
    while num1 or num2:
        sum=0
        if num1:
            sum+=num1.data
            num1=num1.next
        if num2:
            sum+=num2.data
            num2=num2.next
        total_sum=sum+carry
        carry=total_sum//10
        sum_needto_added=total_sum%10
        ptr.next=Node(sum_needto_added)
        ptr=ptr.next
    if carry:
        ptr.next=Node(carry)
    return dummy.next

    
