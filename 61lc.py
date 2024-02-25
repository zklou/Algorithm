n-k n>k 

if! head return null

ListNode cur = head
int n = 1
while cur.next != null:
    cur = cur.next
    n++

    for i=0; i<n-k; i++:
        cur = cur.next
    
    head = cur->next
cur next = nullptr
return head 
