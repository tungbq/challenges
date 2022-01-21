/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
	let last = m + n - 1;

	while (m > 0 && n > 0) {
		if (nums1[m - 1] > nums2[n - 1]) {
			nums1[last] = nums1[m - 1];
			m -= 1;
		} else {
			nums1[last] = nums2[n - 1];
			n -= 1;
		}
		last -= 1;
	}

	while (n > 0) {
		nums1[last] = nums1[n - 1];
		n -= 1;
	}
};

(nums1 = [1, 2, 3, 0, 0, 0]), (m = 3), (nums2 = [2, 5, 6]), (n = 3);
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1

console.log(merge(nums1, m, nums2, n));
