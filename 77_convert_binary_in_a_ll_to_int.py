class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_decimal_value(head: ListNode) -> int:
    res = 0
    while head:
        res = res * 2 + head.val
        head = head.next
    return res