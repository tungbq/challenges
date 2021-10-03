// Link: https://leetcode.com/problems/reverse-string/

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
	let left = 0;
	let right = s.length - 1;

	while (left < right) {
		let tmp = s[left];
		s[left] = s[right];
		s[right] = tmp;
		left += 1;
		right -= 1;
	}
};

s = ['h', 'e', 'l', 'l', 'o'];
reverseString(s);
console.log(s);
// Expected Output: ["o","l","l","e","h"]

// Time: O(n)
// Space: O(1)
