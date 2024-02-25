# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        list3 = ListNode(val = 100, next = None)
        cur3 = list3
        while cur1 != None or cur2 != None:
            if cur1 == None:
                cur3.next = cur2
                cur3=cur3.next
                cur2=cur2.next
            elif cur2 == None:
                cur3.next = cur1
                cur3=cur3.next
                cur1=cur1.next
            elif cur1.val>= cur2.val:               
                cur3.next = cur2
                cur2=cur2.next
                cur3= cur3.next
            else:                
                cur3.next = cur1                
                cur1=cur1.next
                cur3 = cur3.next
        return list3.next

