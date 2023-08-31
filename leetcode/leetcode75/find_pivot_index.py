"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of 
the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""


"""
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
"""

class Solution:
   def pivotIndex(self, nums):
      result = -1
      # Calculate the sum
      sum = 0
      for num in nums:
         sum += num

      # Loop and increase the left sum
      # Solve proplem using the math
      # TODO: find more effective way to solve this issue
      left_sum = 0
      for index in range(len(nums)):
         if index != 0:
            left_sum += nums[index - 1]
         if ((sum - nums[index]) / 2) == left_sum:
            result = index
            break

      return result