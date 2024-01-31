# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        virtual=ListNode(-1)
        virtual.next=ListNode(-1)
        cur=virtual.next
        while list1!=None or list2!=None:
            if list1!=None and list2!=None:
                if list1.val<list2.val:
                    cur.val=list1.val
                    list1=list1.next
                else:
                    cur.val=list2.val
                    list2=list2.next
            elif list1!=None:
                cur.val=list1.val
                list1=list1.next
            elif list2!=None:
                cur.val=list2.val
                list2=list2.next
            else:
                pass
            if list1==None and list2==None:
                    return virtual.next
            cur.next=ListNode(1000)
            cur=cur.next
        return virtual.next


#优化后

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        virtual = ListNode(-1)
        cur = virtual

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # 如果其中一个链表已经遍历完，直接连接另一个链表的剩余部分
        cur.next = list1 if list1 is not None else list2

        return virtual.next