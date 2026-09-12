# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def size(head):
    c=0
    while head:
        c+=1
        head=head.next
    return c
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=size(headA)
        b=size(headB)
        diff=abs(a-b)
        if a>b:
            for _ in range(diff):
                headA=headA.next
        else:
            for _ in range(diff):
                headB=headB.next
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None