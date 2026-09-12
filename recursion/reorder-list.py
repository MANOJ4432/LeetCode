# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mid(head):
    slow,fast=head,head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    return slow
def rev(head):
    prev=None
    while head:
        nex=head.next
        head.next=prev
        prev=head
        head=nex
    return prev
def print_List(head):
    while head:
        print(head.val,end=" ")
        head=head.next
    print()
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        midNode=mid(head)
        temp=midNode.next
        midNode.next=None
        temp=rev(temp)
        print_List(head)
        print_List(temp)
        curr=head
        while head and temp:
            nex=head.next
            head.next=temp
            head=head.next
            temp=temp.next
            head.next=nex
            head=head.next
        return curr
        """ nex=head.nex
            head.next=temp
            temp=temp.next
            head.nex=nex """
        
