class Solution:
    def flatten(self, head):
        def dfs(node):
            cur = node
            last = None

            while cur:
                nxt = cur.next

                if cur.child:
                    tail = dfs(cur.child)

                    cur.next = cur.child
                    cur.child.prev = cur
                    cur.child = None

                    if nxt:
                        tail.next = nxt
                        nxt.prev = tail

                    last = tail
                else:
                    last = cur

                cur = nxt

            return last

        dfs(head)
        return head