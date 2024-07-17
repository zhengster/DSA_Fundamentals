def longest_substring_without_repeating_characters(string):    
    """
    Sliding window problem where you initialize the two pointers i,j on the left side
    of the string and expand the window of unique characters. 
    """ 
    char_set = set()
    max_len = -1 * float('inf')
    # Initialize two pointers to start at the beginning of the array 
    i, j = 0, 0 

    while j < len(string): 
        char = string[j] 
        # If we haven't encountered the char before, add it to the set and increment j (right pointer) 
        if char not in char_set: 
            char_set.add(char) 
            max_len = max(max_len, j - i + 1)
            j += 1
        # Else, remove the char from the set and increment i (left pointer) 
        else: 
            char_set.remove(char) 
            i += 1 
    return max_len 

def container_with_the_most_water(height): 
    """
    Given an array representing heights, find the maximum amount of water 
    stored between any two heights in the array. 
    """
    max_amount = 0 
    i, j = 0, len(height) - 1 
    
    while i < j: 
        if height[i] < height[j]: 
            # Height of the container is always constrained by the lower-value boundary
            max_amount = max(max_amount, height[i] * (j - i))
            i += 1 # Increment i pointer to try to find a taller height 
        else: 
            max_amount = max(max_amount, height[j] * (j - i))
            j -= 1 
    
    return max_amount  

def maximum_subarray(nums): 
    """
    Given an array of numbers, find and return the maximum sum of a subarray. 
    """
    # Keep track of two variables: cur_sum and max_sum (seen so far) 
    cur_sum = nums[0] 
    max_sum = nums[0] 

    for i in range(1, len(nums)): 
        # If cur_sum < 0, then reset it to be 0. 
        # We want to get rid of all the negative prefixes that are decreasing our total sum. 
        if cur_sum < 0:  
            cur_sum = 0 

        cur_sum += nums[i] 
        max_sum = max(max_sum, cur_sum) 
    
    return max_sum 

import unittest 
class TestSlidingWindow(unittest.TestCase):

    def test_longest_substring_without_repeating_characters(self): 
        string = "abcda"
        expected = 4
        self.assertEqual(expected, longest_substring_without_repeating_characters(string))

        string = "abcedf"
        expected = 6 
        self.assertEqual(expected, longest_substring_without_repeating_characters(string))
    
    def test_maximum_subarray(self): 
        nums = [5,4,-1,7,8]
        expected = 23
        self.assertEqual(expected, maximum_subarray(nums)) 

if __name__ == "__main__": 
    unittest.main() 
