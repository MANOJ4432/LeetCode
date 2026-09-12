# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """e=ListNode(-1)
        o=ListNode(-1)
        do=o
        de=e
        while(head):
            if head.val & 1:
                o.next=head
            else:
                e.next=head
        e.next=None
        o.next=de.next
        return  """
        if head is None or head.next is None:
            return head
        e=ListNode(-1)
        o=ListNode(-1)
        do=o
        de=e
        while head.next and head.next.next:
            o.next=head
            o=o.next
            e.next=head.next
            e=e.next
            head=head.next.next
        o.next=head
        o=o.next
        e.next=head.next
        o.next=de.next
        return do.next




