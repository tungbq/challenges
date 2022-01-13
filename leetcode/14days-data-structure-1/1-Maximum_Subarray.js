// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
// A subarray is a contiguous part of an array.

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
	let finalMax = nums[0];
	let currentMax = nums[0];
	for (let i = 0; i < nums.length; i++) {
		currentMax = Math.max(currentMax + nums[i], nums[i]);
		finalMax = Math.max(currentMax, finalMax);
	}
	return finalMax;
};

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.
console.log(maxSubArray(nums));

nums = [-2, 1];
console.log(maxSubArray(nums));
