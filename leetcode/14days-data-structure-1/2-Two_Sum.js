/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
	// sort the array first, O (nlogn)
	sorted_nums = quicksort(nums);

	let left = 0;
	let right = nums.length - 1;
	var result = [];
	while (left < right) {
		if (sorted_nums[left] + sorted_nums[right] === target) {
			result = [left, right];
			break;
		} else if (sorted_nums[left] + sorted_nums[right] > target) {
			right -= 1;
		} else {
			left += 1;
		}
	}
	return result;
};

function quicksort(array) {
	if (array.length <= 1) {
		return array;
	}

	var pivot = array[0];

	var left = [];
	var right = [];

	for (var i = 1; i < array.length; i++) {
		array[i] < pivot ? left.push(array[i]) : right.push(array[i]);
	}

	return quicksort(left).concat(pivot, quicksort(right));
}

// Test case 1:
(nums = [2, 7, 11, 15]), (target = 9);
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

console.log(twoSum(nums, target));

// Test case 2:
(nums = [3, 2, 4]), (target = 6);
// Output: [1,2]
console.log(twoSum(nums, target));
