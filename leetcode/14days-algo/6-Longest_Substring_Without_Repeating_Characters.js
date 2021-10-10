/**
 * @param {string} s
 * @return {number}
 */
// var lengthOfLongestSubstring = function (s) {
// 	str_arr = s.split('');
// 	let maxValue = 0;
// 	let windowEnd = 0;
// 	let track_element = [];

// 	console.log(str_arr);
// 	for (let i = 0; i < str_arr.length; i++) {
// 		if (!track_element.includes(str_arr[i])) {
// 			// Using object to keep track of elements
// 			track_element.push(str_arr[i]);
// 			windowEnd += 1;
// 		} else {
// 			windowEnd -= 1;
// 		}

// 		if (windowEnd > maxValue) {
// 			maxValue = windowEnd;
// 		}
// 	}

// 	return maxValue;
// };

var lengthOfLongestSubstring = function (s) {
	str_arr = s.split('');
	let maxValue = 0;
	let windowStart = 0;
	let windowEnd = 0;
	let track_element = {};

	while (windowEnd < str_arr.length) {
		if (!track_element.hasOwnProperty(str_arr[windowEnd])) {
			// Using object to keep track of elements
			track_element[str_arr[windowEnd]] = 1;
			windowEnd += 1;
			if (Object.keys(track_element).length > maxValue) {
				maxValue = Object.keys(track_element).length;
			}
		} else {
			delete track_element[str_arr[windowStart]];
			windowStart += 1;
		}
		// console.log(track_element);
	}

	return maxValue;
};

s = 'abacabcbb';
// Output: 3
// Explanation: The answer is "abc", with the length of 3

// s = 'bbbbb';
// s = 'pwwkew';
// s = 'a ';
// s = 'aab';
// s = '';
// s = ' ';
// s = 'dvdf';

console.log(lengthOfLongestSubstring(s));
