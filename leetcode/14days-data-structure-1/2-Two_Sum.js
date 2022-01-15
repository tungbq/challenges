/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
	const tracked_nums = {};

	for (let i = 0; i < nums.length; i++) {
		if (nums[i] in tracked_nums) {
			return [tracked_nums[nums[i]], i];
		}

		console.log('Loop ' + i + 'times...');
		const remainder = target - nums[i];

		if (!(remainder in tracked_nums)) {
			tracked_nums[remainder] = i;
		}

		console.log(tracked_nums);
	}
};

// Test case 1:
(nums = [2, 7, 11, 15]), (target = 9);
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

console.log(twoSum(nums, target));

// Test case 2:
(nums = [3, 2, 4]), (target = 6);
// Output: [1,2]
console.log(twoSum(nums, target));
