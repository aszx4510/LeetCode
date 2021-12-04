
# 24. Swap Nodes in Pairs

# https://leetcode.com/problems/swap-nodes-in-pairs/
# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11030/My-accepted-java-code.-used-recursion.
# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11030/My-accepted-java-code.-used-recursion./11888



class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Recursive version, lower performance
        if not head or not head.next:
            return head
        _next = head.next
        head.next = self.swapPairs(head.next.next)
        _next.next = head
        return _next


        # Iteration version, higer performance
        if not head or not head.next:
            return head
        current = head
        new_head = head.next
        while current and current.next:
            temp = current
            current = current.next
            temp.next = current.next
            current.next = temp
            current = temp.next

            if current and current.next:  # Set 1 -> 4
                temp.next = current.next
        return new_head
