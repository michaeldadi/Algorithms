class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None


# Floyd cycle detection algorithm
def detect_loop(head):
    slow_ptr = head
    fast_ptr = head
    while (slow_ptr is not None) and (fast_ptr is not None) and (fast_ptr.next is not None):
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            return True

    return False
