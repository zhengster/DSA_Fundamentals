##############
# ARRAYS 
##############
# BUBBLE
def bubble_sort(arr): 
    """
    The largest element "bubbles" to the right. 

    Time complexity: O(n^2) 
    Space complexity: O(1) - no extra space used 
    """
    for i in range(len(arr) - 1): 
        swapped = False 

        for j in range(1, len(arr)): 
            if arr[j] < arr[j - 1]: 
                swapped = True 
                arr[j - 1], arr[j] = arr[j], arr[j - 1] 
        
        # If no elements were swapped during this iteration, the array is already sorted. Terminate. 
        if not swapped: 
            break 
    return arr 

# INSERTION 
def insertion_sort(arr): 
    """
    Insert the element into the correct location in the sorted 
    portion of the list.

    Has a worst case runtime of O(n^2), or more accurately 
    O(n) + f(n), where f(n) = # of inversions.
    """
    for i in range(len(arr)): 
        j = i 
        # If there are no inversions, (list is sorted) this while loop is never entered, so runtime is O(n)
        while j > 0 and arr[j - 1] > arr[j]: 
            arr[j - 1], arr[j] = arr[j], arr[j - 1] 
            j -= 1 
    return arr 
    

# SELECTION 
def selection_sort(arr): 
    """
    Select the minimum during each iteration and swap it into the sorted portion. 
    Has a worst case runtime of O(n^2) when the list is completely reversed. 
    """
    for i in range(len(arr) - 1): 
        min_ind = i 
        # Start iterating from (i + 1) because we assume that arr[0:i] is already sorted
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]: 
                min_ind = j 
        
        # Swap old minimum with new minimum 
        if min_ind != i: 
            arr[min_ind], arr[i] = arr[i], arr[min_ind] 
    
    return arr 

# COUNTING SORT

# RADIX SORT

# HEAP SORT
def heap_sort(arr): 
    pass 

# QUICK SORT
def quick_sort(arr): 
    pass 

# MERGE SORT 
def merge_sort(arr): 
    if len(arr) <= 1: 
        return arr 

    # Find the middle of the array, split into two subarrays
    middle = len(arr) // 2
    arr_1 = arr[0:middle]

    # Recursively perform merge sort on each subarray 
    arr_2 = arr[middle:]
    arr_1 = merge_sort(arr_1) 
    arr_2 = merge_sort(arr_2) 

    # Merge the two subarrays and return 
    return merge(arr_1, arr_2) 

def merge(arr_1, arr_2): 
    i, j = 0, 0 
    res = []

    while i < len(arr_1) and j < len(arr_2): 
        if arr_1[i] < arr_2[j]: 
            res.append(arr_1[i])
            i += 1
        else: 
            res.append(arr_2[j])
            j += 1
    
    # Merge in remaining elements
    while i < len(arr_1): 
        res.append(arr_1[i])
        i += 1
    while j < len(arr_2): 
        res.append(arr_2[j])
        j += 1

    return res 

import unittest

class TestArraySortMethods(unittest.TestCase):

    def test_bubble(self): 
        array = [10, 9, 11, 13, 7, 2, 3]
        sorted_array = [2, 3, 7, 9, 10, 11, 13]
        self.assertEqual(bubble_sort(array), sorted_array)
    
    def test_insertion(self): 
        array = [10, 9, 11, 13, 7, 2, 3]
        sorted_array = [2, 3, 7, 9, 10, 11, 13]
        self.assertEqual(insertion_sort(array), sorted_array)
    
    def test_selection(self): 
        array = [10, 9, 11, 13, 7, 2, 3]
        sorted_array = [2, 3, 7, 9, 10, 11, 13]
        self.assertEqual(selection_sort(array), sorted_array)
    
    def test_merge(self): 
        array = [10, 9, 11, 13, 7, 2, 3]
        sorted_array = [2, 3, 7, 9, 10, 11, 13]
        self.assertEqual(merge_sort(array), sorted_array)

if __name__ == '__main__':
    unittest.main()


