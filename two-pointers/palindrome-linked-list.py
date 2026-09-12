# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mid(head):
    slow=head
    fast=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    return slow
def rev(head):
    prev=None
    while(head):
        nex=head.next
        head.next=prev
        prev=head
        head=nex
    return prev
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return True
        midNode=mid(head)
        temp=midNode.next
        temp=rev(temp)
        while(temp and head):
            if temp.val!=head.val:
                return False
            temp=temp.next
            head=head.next
        return True




        