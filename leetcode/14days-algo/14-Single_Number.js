/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
	let res = 0;
	for (let i = 0; i < nums.length; i++) {
		res ^= nums[i];
	}

	return res;
};

// Input:
nums = [4, 1, 2, 1, 2];
// Output: 4

console.log(singleNumber(nums));
