class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

#set 会比较对象的hash地址， 唯一



#快慢指针


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast:
            if fast.next is None:
                return False
            if fast == slow: #比较的是两个实例是否为同一个实例，即它们在内存中的地址是否相同
                return True
            slow = slow.next
            fast = fast.next.next
        return False