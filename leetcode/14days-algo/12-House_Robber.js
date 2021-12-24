/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
	let rob1 = 0;
	let rob2 = 0;

	for (const n of nums) {
		maxValue = Math.max(n + rob1, rob2);
		rob1 = rob2;
		rob2 = maxValue;
	}

	return maxValue;
};

nums = [1, 2, 3, 1];
// Output: 4
// Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
// Total amount you can rob = 1 + 3 = 4.

console.log(rob(nums));
