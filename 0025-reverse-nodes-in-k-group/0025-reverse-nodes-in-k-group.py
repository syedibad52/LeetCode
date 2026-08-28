class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            end = prev
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next

            curr = prev.next
            nxt = end.next

            p = nxt
            while curr != nxt:
                temp = curr.next
                curr.next = p
                p = curr
                curr = temp

            temp = prev.next
            prev.next = end
            prev = temp