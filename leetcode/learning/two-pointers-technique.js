// Two sum

// -> For this implementation, input array must be sorted first
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Output: Because nums[0] + nums[1] == 9, we return [0, 1]

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    cur_sum = nums[left] + nums[right];
    if (cur_sum < target) {
      left += 1;
    } else if (cur_sum > target) {
      right -= 1;
    } else {
      // Found the result, return index of those elements
      return [left, right];
    }
  }

  // Not found any element meet requirement, return [-1, -1]
  return [-1, -1];
};

// Expected [0, 1]
nums = [2,7,11,15], target = 9
let result = twoSum(nums, target)
console.log(result)

// Expected [1, 2]
nums1 = [2,3,4], target1 = 6
let result1 = twoSum(nums1, target1)
console.log(result1)
