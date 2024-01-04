class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def ll_has_cycle_with_set(head: ListNode) -> bool:
    seen = set()

    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next

    return False

def ll_has_cycle_with_2_ptrs(head: ListNode) -> bool:
    if not head:
        return False
    
    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False