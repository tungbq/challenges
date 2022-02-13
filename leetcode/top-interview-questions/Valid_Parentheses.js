/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
	const open_brackets = ['{', '[', '('];
	const close_brackets = ['}', ']', ')'];
	let track_open_elements = [];

	// loop through each char
	for (let i = 0; i < s.length; i++) {
		if (open_brackets.includes(s[i])) {
			// in case string ends of with open brackets, treat it as 'false'
			if (i === s.length - 1) {
				return false;
			}

			track_open_elements.push(s[i]);
		} else {
			// case close bracket
			if (
				close_brackets.indexOf(s[i]) !==
				open_brackets.indexOf(track_open_elements.pop())
			) {
				return false;
			}
		}

		// cover case open brackets > close brackets
		if (i === s.length - 1 && track_open_elements.length > 0) {
			return false;
		}
	}
	// check each pair
	return true;
};

// Test case 1:
// Input:
s = '()[]{}';
// Output: true
console.log('-----Output----');
console.log(isValid(s));

// Test case 2:
// Input:
s = '{[()]}';
// Output: true
console.log('-----Output----');
console.log(isValid(s));

// Test case 3:
// Input:
s = '[';
// Output: false
console.log('-----Output----');
console.log(isValid(s));

// Test case 4:
// Input:
s = '"([]"';
// Output: false
console.log('-----Output----');
console.log(isValid(s));

// Test case 5:
// Input:
s = '[])';
// Output: false
console.log('-----Output----');
console.log(isValid(s));
