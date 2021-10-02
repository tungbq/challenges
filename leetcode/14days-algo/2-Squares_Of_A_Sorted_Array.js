// Link: https://leetcode.com/problems/squares-of-a-sorted-array/

// Using two pointers
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function (nums) {
	// Determine the right element
  let right = 0;
  while (right < nums.length && nums[right] < 0) {
    right += 1;
  }
  left = right - 1;

  output = [];
  while (left >=0 && right < nums.length) {
    if (Math.pow(nums[left], 2) < Math.pow(nums[right], 2)) {
      output.push(Math.pow(nums[left], 2));
      left -= 1;
    } else {
      output.push(Math.pow(nums[right], 2));
      right += 1;
    }
  }

  while (left >= 0) {
    output.push(Math.pow(nums[left], 2));
    left -= 1;
  }

  while (right < nums.length) {
    output.push(Math.pow(nums[right], 2));
    right += 1;
  }

  return output;
};

nums = [-4,-1,0,3,10]
console.log(sortedSquares(nums));
// Expected: [0,1,9,16,100]
