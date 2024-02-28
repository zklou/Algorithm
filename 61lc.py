# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        cur1 = head
        cur2 = head
        cur3 = head
        n = 0
        i = 0
        p = 0
        q = 0
        while cur1 != None:
            n = n + 1
            cur1 = cur1.next
        if k >= n:
            k = k % n

        while i < (n - k):
            i = i + 1
            cur2 = cur2.next
        
        cur1 = head
        while p < n - 1:
            p = p + 1
            cur1 = cur1.next
        cur1.next = head

        cur1 = head
        while q < k:
            q = q + 1
            cur1 = cur1.next
        cur3 = cur1.next
        cur1.next = None
        
        return cur3
