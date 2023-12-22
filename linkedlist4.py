class singlyLinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head
def PrintLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
#example usage
def createdLinkedList(elements):
    if not elements:
        return None
    head = singlyLinkedListNode(elements[0]) 
    current = head
    for data in elements[1:]:
        current.next = singlyLinkedListNode(data) 
        current = current.next
    return head
test_cases = 1 
test_data = [[1, 2, 3, 4, 5]]
for _ in range(test_cases):
    head = createdLinkedList(test_data[_])
    print("Original Linked List:") 
    PrintLinkedList(head)
    head = reverse(head) 
    print("\nReversed Linked List:")
    PrintLinkedList(head)                            
