/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
	const result = [];
	for (let i = 0; i < nums.length; i++) {
		const element = nums[i];
		let smallerCount = 0;
		for (let j = 0; j < nums.length; j++) {
			if (nums[j] < element) {
				smallerCount++;
			}
		}
		result.push(smallerCount);
	}

	return result;
};

nums = [8, 1, 2, 2, 3];
// Expected Output: [4,0,1,1,3]

console.log(smallerNumbersThanCurrent(nums));

// O(n^2) time comflexity solution

// TODO: Will find a better way to resolve the issue

