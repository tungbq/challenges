// Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

// Example 1:
// Input: s = "leetcode"
// Output: 0

// Example 2:
// Input: s = "loveleetcode"
// Output: 2

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
	// Convert to array first.
	s = s.split('');
	// Tracking element with freq using map
	let track_item = {};
	for (let i = 0; i < s.length; i++) {
		if (!(s[i] in track_item)) {
			track_item[s[i]] = 1;
		} else {
			track_item[s[i]] += 1;
		}
	}
	// Processing map to get result
	for (char in track_item) {
		if (track_item[char] === 1) {
			return s.indexOf(char);
		}
	}
	// Not found any unique char
	return -1;
};

s = 'loveleetcode';
s = 'ttung';
console.log(firstUniqChar(s));
