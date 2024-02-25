# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        list3 = ListNode(100)
        list3.next = head
        cur3 = list3

        while cur3.next and cur3.next.next:
            cur1 = cur3.next
            cur2 = cur1.next
            next_pair = cur2.next 
            
            cur3.next = cur2
            cur2.next = cur1
            cur1.next = next_pair
            
            cur3 = cur1
        return list3.next

