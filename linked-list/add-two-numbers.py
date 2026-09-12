# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def size(head):
    c=0
    while head:
        c+=1
        head=head.next
    return c
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        temp=dummy
        dummy.next=l1
        carry=0
        prev=None
        while l1 and l2:
            prev=l2
            value=l1.val+l2.val+carry
            digit=value%10
            carry=value//10
            l1.val=digit
            l1=l1.next
            l2=l2.next
            dummy=dummy.next
        while l1:
            value=l1.val+carry
            digit=value%10
            carry=value//10
            l1.val=digit
            l1=l1.next
            dummy=dummy.next
        
        if l2 is not None:
            prev.next=None
            dummy.next=l2
            while l2:
                value=l2.val+carry
                digit=value%10
                carry=value//10
                l2.val=digit
                l2=l2.next
                dummy=dummy.next
        if carry!=0:
            dummy.next=ListNode(carry)
        return temp.next
        
                






        