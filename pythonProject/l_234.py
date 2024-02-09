class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.head = head
        data = self.appendList()
        return data == data[::-1]

    def appendList(self):
        nums = list()
        cur_node = self.head
        while cur_node:
            nums.append(cur_node.val)
            cur_node = cur_node.next
        return nums