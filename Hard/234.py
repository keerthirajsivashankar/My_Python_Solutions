from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        temp = head
        while stack:
            top = stack.pop()
            if top != temp.val:
                return False
            temp = temp.next
        return True

def create_linked_list(arr: list) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def get_list_input() -> List[int]:
    while True:
        try:
            input_str = input("Enter linked list elements separated by spaces (e.g., '1 2 3 2 1'): ")
            elements = [int(x) for x in input_str.split()]
            return elements
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()

    print("--- Check if Linked List is a Palindrome ---")
    
    list_elements = get_list_input()
    head = create_linked_list(list_elements)
    
    result = sol.isPalindrome(head)
    
    if result:
        print("The linked list is a palindrome.")
    else:
        print("The linked list is NOT a palindrome.")