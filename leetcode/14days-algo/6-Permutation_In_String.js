/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
	s1_arr = s1.split('');
	s2_arr = s2.split('');

	if (s1_arr.length > s2_arr.length) {
		return false;
	}

	let s1_hash_element = {};
	let s2_hash_element = {};

	for (let i = 0; i < s1_arr.length; i++) {
		if (!s1_hash_element.hasOwnProperty(s1_arr[i])) {
			// Using object to keep track of elements
			s1_hash_element[s1_arr[i]] = 1;
		} else {
			s1_hash_element[s1_arr[i]] += 1;
		}
	}

	let windowStart = 0;
	let windowEnd = 0;

	while (windowEnd < s2_arr.length) {
		if (!s2_hash_element.hasOwnProperty(s2_arr[windowEnd])) {
			s2_hash_element[s2_arr[windowEnd]] = 1;
		} else {
			s2_hash_element[s2_arr[windowEnd]] += 1;
		}

		if (windowEnd - windowStart >= s1_arr.length - 1) {
			if (compareTwoObjects(s2_hash_element, s1_hash_element)) {
				return true;
			}

			if (s2_hash_element[s2_arr[windowStart]] > 1) {
				s2_hash_element[s2_arr[windowStart]] -= 1;
			} else {
				delete s2_hash_element[s2_arr[windowStart]];
			}
			windowStart++;
		}

		windowEnd++;
	}

	return false;
};

const compareTwoObjects = (o1, o2) => {
	for (var p in o1) {
		if (o1.hasOwnProperty(p)) {
			if (o1[p] !== o2[p]) {
				return false;
			}
		}
	}
	for (var p in o2) {
		if (o2.hasOwnProperty(p)) {
			if (o1[p] !== o2[p]) {
				return false;
			}
		}
	}
	return true;
};

// Input:
// (s1 = 'ab'), (s2 = 'eidbaooo');
// Output: true
// Explanation: s2 contains one permutation of s1 ("ba").

// Input:
// (s1 = 'ab'), (s2 = 'eidboaoo');
// Output: false

// (s1 = 'ab'), (s2 = 'ab');
// Output: true

(s1 = 'adc'), (s2 = 'dcda');
// Output: true

console.log(checkInclusion(s1, s2));
