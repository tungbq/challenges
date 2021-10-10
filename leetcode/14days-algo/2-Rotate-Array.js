/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var rotate = function (nums, k) {
	k = k % nums.length;
	if (k === 0) return;

	let left = 0;
	let right = nums.length - 1;
	while (left < right) {
		// Swap left, right
		tmp = nums[left];
		nums[left] = nums[right];
		nums[right] = tmp;
		left += 1;
		right -= 1;
	}

	left = 0;
	right = k - 1;
	while (left < right) {
		// Swap left, right
		tmp = nums[left];
		nums[left] = nums[right];
		nums[right] = tmp;
		left += 1;
		right -= 1;
	}

	left = k;
	right = nums.length - 1;
	while (left < right) {
		// Swap left, right
		tmp = nums[left];
		nums[left] = nums[right];
		nums[right] = tmp;
		left += 1;
		right -= 1;
	}
};

(nums = [1, 2, 3, 4, 5, 6, 7]), (k = 3);
// Expected output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]

// (nums = [-1]), (k = 2);
// [undefined,-1]

rotate(nums, k);
console.log(nums);
