/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function (n) {
	let i = 1;

	while (i < n) {
		i *= 2;
	}

	if (i === n) {
		return true;
	}

	return false;
};

n = 5000;
console.log(isPowerOfTwo(n));
// Output: false

n = 128;
console.log(isPowerOfTwo(n));
// Output: true
