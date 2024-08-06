"""
Ref: https://leetcode.com/problems/unique-number-of-occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true 
"""

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
      # define a dict to hold/memorize the value
      # if 'x' element in the dict => increase number
      # check at the end

      occurs = {}

      for num in arr:
        # check if number exists in the occurs or not?
        if num not in occurs:
          occurs[num] = 1
        else:
          occurs[num] += 1
      for k, v in occurs:

      print(occurs)

"""
1: 3
2: 2
3: 1
"""

arr = [1,2,2,1,1,3]

sol = Solution()
sol.uniqueOccurrences(arr)