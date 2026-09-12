# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def size(h):
    c=0
    while h:
        c+=1
        h=h.next
    return c
def intersection(h1,h2):
    a=size(h1)
    b=size(h2)
    diff=abs(a-b)
    maxi=max(a,b)
    if maxi==a:
        for _ in range(diff):
            h1=h1.next
    else:
        for _ in range(diff):
            h2=h2.next
   
    while h1 and h2:
        if h1 is h2:
            return h1
        h1=h1.next
        h2=h2.next
    return inter
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None 
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow is fast:
                break
        else:
            return None
        temp=slow.next
        slow.next=None
        return intersection(temp,head)