class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverse_linked_list(head: ListNode):
    prev = None
    cur = head

    while cur.next:
        cur = cur.next
        cur.next = prev
        prev = cur
    return prev