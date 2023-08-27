"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
         """
         Do not return anything, modify nums in-place instead.
         """
         left = 0
         right = 0
         while left < len(nums) and right < len(nums):
            # Move if left is non-zero
            if nums[left] != 0:
               left += 1
               right += 1
               continue

            if nums[right] == 0:
               right += 1
               continue

            if nums[left] == 0 and nums[right] != 0:
               # swap these values
               nums[left] = nums[right]
               nums[right] = 0
               left += 1
               continue
         return nums
