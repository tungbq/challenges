"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value
and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""
 
"""
Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
"""

class Solution:
    def findMaxAverage(self, nums, k):
        cur_sum = 0
        result = float('-inf')
        print("===")
        print(len(nums))
        print(k)
        for i in range(len(nums)):
          # init the sum
          if i < k:
            cur_sum += nums[i]
            if (i == (k-1)):
              result = cur_sum
          else:
            # slicing approach
            cur_sum += nums[i] - nums[i - k]
          if cur_sum > result:
            result = cur_sum
        return result / k
