# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def midFind(head):
    if head is None or head.next is None:
        return head
    slow=head
    fast=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    return slow
def merge(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.val < head2.val:
        dummy=head1
        head1=head1.next
    else:
        dummy=head2
        head2=head2.next
    temp=dummy
    while head1!=None and head2!=None:
        if head1.val < head2.val:
            dummy.next=head1
            head1=head1.next
        else:
            dummy.next=head2
            head2=head2.next
        dummy=dummy.next
    if head1!=None:
        dummy.next=head1
    if head2!=None:
        dummy.next=head2
    return temp
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        mid=midFind(head)
        temp=mid.next
        mid.next=None
        return merge(self.sortList(head),self.sortList(temp))
