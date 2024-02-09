class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        index = 0

        while index != n:
            fast = fast.next
            index += 1
        
        if not fast:
            return head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head