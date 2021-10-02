// Move Zeroes
// Link: https://leetcode.com/problems/move-zeroes/
// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
// Note that you must do this in-place without making a copy of the array.

// Two-pointers

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
	let left = 0;
	let right = 0;

	while (right < nums.length) {
		if (nums[right] !== 0) {
			// Swap nums[left] and nums[right]
			tmp = nums[right];
			nums[right] = nums[left];
			nums[left] = tmp;
			left += 1;
		}

		right += 1;
	}
};

nums = [0, 1, 0, 3, 12];

moveZeroes(nums);
console.log(nums);
// Expected output: [1,3,12,0,0]
