/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
	// loop through each char
	for (let i = 0; i < s.length; i += 2) {
		if (
			s[i] + s[i + 1] !== '[]' &&
			s[i] + s[i + 1] !== '()' &&
			s[i] + s[i + 1] !== '{}'
		) {
			return false;
		}
	}
	// check each pair
	return true;
};

// Test case 1:
// Input:
s = '()[]{}{';
// Output: true
console.log('-----Output----');
console.log(isValid(s));

// Test case 2:
// TODO: Cover this case
// Input:
s = '{[]}';
// Output: true
console.log('-----Output----');
console.log(isValid(s));
