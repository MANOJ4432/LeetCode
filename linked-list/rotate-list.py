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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        n=size(head)
        k=k%n
        if k==0:
            return head
        temp=head
        slow,fast=head,head
        for _ in range(k):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        new_head=slow.next
        slow.next=None
        fast.next=temp
        return new_head