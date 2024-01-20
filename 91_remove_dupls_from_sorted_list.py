class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def delete_duplicates(head: ListNode) -> ListNode:
    if head == None:
        return

    dummy = head
    while head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next

    return dummy