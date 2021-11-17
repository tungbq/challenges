/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
	const equals = (a, b) => JSON.stringify(a) === JSON.stringify(b);

	const number_array = x.toString().split('');
	console.log(number_array);
	let left = 0;
	let right = number_array.length - 1;

	while (left < right) {
		// Swap elements
		tmp = number_array[left];
		number_array[left] = number_array[right];
		number_array[right] = tmp;
		left++;
		right--;
	}
	console.log(number_array);
	return equals(number_array, x.toString().split(''));
};

x = 121;
// Output: true
console.log(isPalindrome(x));

// TODO: Improve run time
