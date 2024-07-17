###############
# LINKED LISTS
###############
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __eq__(self, other):
        # Compare two linked lists by their values and structure
        # This equals method is necessary in order for the code to compare equality of the linked lists, NOT just compare their addresses in memory 
        if not isinstance(other, ListNode):
            return False
        current_self = self
        current_other = other
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None


def insertion_sort(head): 
    """
    EXAMPLE: 
    1->2->4->6->5
    prev = 6 
    cur = 5
    tmp = 4 
    tmp.next = 6 

    GOAL: Insert cur in between tmp and tmp.next. 
    HINT: It's currently something like tmp --> tmp.next ... prev --> cur --> cur.next. 
    WANT: tmp --> cur --> tmp.next ... prev --> cur.next
    """
    dummy = ListNode(None, head) 
    prev, cur = head, head.next 

    while cur: 
        # If the positions of the nodes relative to each other are correct, advance prev and cur and continue 
        if cur.val >= prev.val: 
            prev = cur 
            cur = cur.next 
            continue 
        
        # Else, perform the swapping of the pointers
        tmp = dummy 
        # Move tmp until tmp.next.val <= cur.val. 
        while cur.val > tmp.next.val: 
            tmp = tmp.next 
        
        # Now we could have something like tmp --> tmp.next --> prev --> cur --> cur.next
        # We want to have tmp --> cur --> tmp.next --> prev --> cur.next (e.g. insert cur in between tmp and tmp.next)
        prev.next = cur.next
        cur.next = tmp.next 
        tmp.next = cur 
        # Advance the cur pointer 
        cur = prev.next # = cur.next 
        # Now we have n --> n --> n --> prev --> cur 
    return dummy.next

def merge_sort(head):
    """
    :type head: ListNode
    :rtype: ListNode
    
    O(n log n): Merge sort! But this won't be constant space complexity. 
    """
    if not head or not head.next: 
        return head  # REMEMBER THIS Base case: return head if the list is empty or has only one node

    # Cut list in half 
    list1 = head
    list2 = get_middle_of_linked_list(head) 
    # For list1, set the middle node's next to None (to get rid of the portion of the list after the midpoint) 
    original_list2_next = list2.next 
    list2.next = None
    list2 = original_list2_next
    
    list1 = merge_sort(list1) 
    list2 = merge_sort(list2) 
    return merge_two_sorted_linked_lists(list1, list2) 

def get_middle_of_linked_list(head): 
    # Use fast and slow pointers!
    slow, fast = head, head.next
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next 
    return slow

def insert_element_in_sorted_linked_list(head, element): 
    """
    Suppose you have a list: 1 -> 2 -> 3 -> 5, and you want to insert 4. 
    We need to find where the condition (head.next.val <= element.val) is no true. 
    That's when head = 3, head.next = 5. So we insert 4 in between 3 and 5. 
    """
    head_copy = head

    while head.next and head.next.val <= element.val: 
        head = head.next 
    
    # Assign head.next = element, element.next = original head.next
    original_next = head.next 
    head.next = element 
    element.next = original_next

    return head_copy 


def merge_two_sorted_linked_lists(head1, head2): 
    # Initialize dummy node to point to beginning of merged result and tail pointer to store the current node 
    dummy = tail = ListNode() # Set tail equal to the dummy so that the dummy can eventually reference the start of the merged portion 

    while head1 and head2: 
        if head1.val < head2.val: 
            # Common mistake: setting tail = head1 simply updates tail to the same memory address as head1. tail would just "bounce" between being set equal to head1 and head2's nodes
            tail.next = head1 # Remember to set tail.NEXT equal to the next thing! 
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next # Advance the tail pointer

    # Merge in the remaining nodes (only one of the lists will have remaining nodes) 
    if head1: 
        tail.next = head1
    elif head2: 
        tail.next = head2

    return dummy.next # Remember to return dummy.next, not dummy. This works because at the beginning, tail was equal to dummy and tail.next was set equal to head.next.

def reverse_linked_list_iter(head): 
    prev, cur = None, head 
    while cur: 
        next = cur.next 
        cur.next = prev 
        prev = cur 
        cur = next 
    return prev 

def reverse_linked_list_recursive(head): 
    """
    For a list 1 -> 2 -> 3:

    The first call: reverse_linked_list_recursive(1):
    Calls reverse_linked_list_recursive(2):
    Calls reverse_linked_list_recursive(3):
    Returns 3 because the base case is met (head.next is None).
    Reverses the link: 2.next.next = 2 and 2.next = None.
    Returns 3 (new head of the partially reversed list).
    Reverses the link: 1.next.next = 1 and 1.next = None.
    Returns 3 (new head of the fully reversed list).
    The linked list is now 3 -> 2 -> 1.
    """
    if head is None or head.next is None: 
        return head 
    # Recursively reverse the linked list 
    new_head = reverse_linked_list_recursive(head.next) 
    head.next.next = head # Point head's next back to head 
    head.next = None # Make head's next None, i.e. make head the end of the linked list 
    return new_head
     


import unittest 

class TestLinkedListMethods(unittest.TestCase): 
    def test_insertion(self): 
        head = ListNode(4, ListNode(2, ListNode(1, ListNode(3, None))))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
        self.assertEqual(expected, insertion_sort(head))
    
    def test_merge_two_sorted_lists(self): 
        head1 = ListNode(1, ListNode(3, ListNode(5)))
        head2 = ListNode(2, ListNode(4))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(expected, merge_two_sorted_linked_lists(head1, head2))
    
    def test_insert_element_in_sorted_list(self): 
        head = ListNode(1, ListNode(3, ListNode(5)))
        element = ListNode(4, None) 
        expected = ListNode(1, ListNode(3, ListNode(4, ListNode(5))))
        self.assertEqual(expected, insert_element_in_sorted_linked_list(head, element))

        head = ListNode(1, ListNode(2, ListNode(3)))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertEqual(expected, insert_element_in_sorted_linked_list(head, element))
    
    def test_merge_sort(self): 
        head = ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertEqual(expected, merge_sort(head)) 
    
    def test_reverse_linked_list_iter(self): 
        head = ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertEqual(expected, reverse_linked_list_iter(head)) 
    
    def test_reverse_linked_list_recursive(self):
        head = ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertEqual(expected, reverse_linked_list_recursive(head)) 
       

if __name__ == "__main__": 
    unittest.main() 
