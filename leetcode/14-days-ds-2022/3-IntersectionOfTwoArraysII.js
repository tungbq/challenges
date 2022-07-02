// Given two integer arrays nums1 and nums2, return an array of their intersection.
// Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

// Example 1:
// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2,2]

// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [4,9]
// Explanation: [9,4] is also accepted.

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
	const result = [];
	for (let i = 0; i < nums1.length; i++) {
		let is_pushed = false;
		for (let j = 0; j < nums2.length; j++) {
			if (nums1[i] == nums2[j] && !is_pushed) {
				result.push(nums1[i]);
				nums2.splice(j, 1);
				is_pushed = true;
			}
		}
	}
	return result;
};

// nums1 = [2, 1];
// nums2 = [1, 2];

console.log(intersect(nums1, nums2));
