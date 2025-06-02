class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def removeDuplicates(self, head: Node) -> Node:
        curr = head
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

def create_linked_list(arr: list) -> Node:
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head

def print_linked_list(head: Node):
    current = head
    elements = []
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" -> ".join(elements))

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Duplicates present
    arr1 = [1, 1, 2, 3, 3, 3, 4, 5, 5]
    head1 = create_linked_list(arr1)
    print("Original List 1:")
    print_linked_list(head1)
    
    new_head1 = sol.removeDuplicates(head1)
    print("List 1 after removing duplicates:")
    print_linked_list(new_head1)
    # Expected Output: 1 -> 2 -> 3 -> 4 -> 5

    # Test Case 2: No duplicates
    arr2 = [1, 2, 3, 4, 5]
    head2 = create_linked_list(arr2)
    print("\nOriginal List 2:")
    print_linked_list(head2)
    
    new_head2 = sol.removeDuplicates(head2)
    print("List 2 after removing duplicates:")
    print_linked_list(new_head2)
    # Expected Output: 1 -> 2 -> 3 -> 4 -> 5

    # Test Case 3: All duplicates
    arr3 = [7, 7, 7, 7]
    head3 = create_linked_list(arr3)
    print("\nOriginal List 3:")
    print_linked_list(head3)
    
    new_head3 = sol.removeDuplicates(head3)
    print("List 3 after removing duplicates:")
    print_linked_list(new_head3)
    # Expected Output: 7

    # Test Case 4: Empty list
    arr4 = []
    head4 = create_linked_list(arr4)
    print("\nOriginal List 4:")
    print_linked_list(head4)
    
    new_head4 = sol.removeDuplicates(head4)
    print("List 4 after removing duplicates:")
    print_linked_list(new_head4)
    # Expected Output: (empty line)

    # Test Case 5: Single element list
    arr5 = [10]
    head5 = create_linked_list(arr5)
    print("\nOriginal List 5:")
    print_linked_list(head5)
    
    new_head5 = sol.removeDuplicates(head5)
    print("List 5 after removing duplicates:")
    print_linked_list(new_head5)
    # Expected Output: 10