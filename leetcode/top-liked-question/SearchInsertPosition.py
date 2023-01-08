class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        out_index = 0
        for i in range(len(nums)):
            # Handle basic case - match
            if nums[i] == target:
                out_index = i
                break
            # Handle basic case - min
            if target < nums[0]:
                out_index = 0
                break
            # Handle basic case - max
            if target > nums[len(nums)-1]:
                out_index = len(nums)
                break
            if ((nums[i] < target) and (target < nums[i+1])):
                out_index = i+1
                break
        return out_index