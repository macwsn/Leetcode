# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        x = ListNode()
        z = x
        y = set(nums)
        if not head: return None
        while head.next:
            if head.val not in y:
                x.next = ListNode(val=head.val)
                x = x.next
            head = head.next
        if head and head.val not in y:
            x.next = ListNode(val=head.val)
            x = x.next
        return z.next if z.next else z