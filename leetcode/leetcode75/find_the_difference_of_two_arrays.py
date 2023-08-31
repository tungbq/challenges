"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

class Solution:
    def findDifference(self, nums1, nums2):
        # Reducing the array size by converting it to set
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        nums1_res = self.baseFindDifference(nums1_set, nums2_set)
        nums2_res = self.baseFindDifference(nums2_set, nums1_set)
        return [nums1_res, nums2_res]

    def baseFindDifference(self, nums1, nums2):
        result = []
        for num1 in nums1:
            if num1 not in nums2 and num1 not in result:
                result.append(num1)
        return result