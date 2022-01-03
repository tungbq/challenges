/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
	const nums_tracking = {};

	for (num of nums) {
		if (num in nums_tracking) {
			return true;
		}

		nums_tracking[num] = 1;
	}

	return false;
};

nums = [1, 2, 3, 1];
// Output: true
console.log(containsDuplicate(nums));

nums = [1, 2, 3, 4];
console.log(containsDuplicate(nums));
// Output: false
