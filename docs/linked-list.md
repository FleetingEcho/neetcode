```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#翻转linked list
def reverse_list(head):
    prev = None
    cur = head
    while cur:
        temp = cur.next

        cur.next = prev
        prev = cur

        cur = temp
    return prev

```

常见策略:
1.虚拟节点 `pre=ListNode(-1)`
