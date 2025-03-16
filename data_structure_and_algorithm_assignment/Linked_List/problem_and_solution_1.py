## Problem Statement:
## Given the head of a singly linked list, reverse the list and return its new head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example Usage
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original List:")
printList(head)

reversed_head = reverseList(head)
print("Reversed List:")
printList(reversed_head)

# Output
# Original List:
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# Reversed List:
# 5 -> 4 -> 3 -> 2 -> 1 -> None



# Explanation
#I initialize prev as None and traverse the list while keeping track of the next node.
#I change the next pointer of each node to point to the previous node.
#At the end, prev will be the new head.