// Recursion / Backtracking

/**
 * @param {number[]} nums
 * @return {number[][]}
 */

var permute = function (nums, set = [], answers = []) {
	// base case
	if (nums.length === 0) answers.push([...set]);

	for (let i = 0; i < nums.length; i++) {
		const newNums = nums.filter((n, index) => index !== i);
		set.push(nums[i]);
		permute(newNums, set, answers);
		set.pop();
    console.log(set)
	}

	return answers;
};

nums = [1, 2, 3];
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

// Input: nums = [0,1]
// Output: [[0,1],[1,0]]

console.log(permute(nums));
