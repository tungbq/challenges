/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
	const new_arr = [];
	for (let i = 0; i < nums.length; i++) {
		if (i < k) {
			new_arr[i] = nums[nums.length - k + i];
		} else {
			new_arr[i] = nums[i - k];
		}
	}
	return new_arr;
};

(nums = [1, 2, 3, 4, 5, 6, 7]), (k = 3);
// Expected output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
console.log(rotate(nums, k));
