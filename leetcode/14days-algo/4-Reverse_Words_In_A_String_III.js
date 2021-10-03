/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
	let output = '';
	const s_arr = s.split(' ');
	let isFirstElement = true;

	for (var word of s_arr) {
		word = word.split('');
		let left = 0;
		let right = word.length - 1;

		while (left < right) {
			let tmp = word[left];
			word[left] = word[right];
			word[right] = tmp;
			left += 1;
			right -= 1;
		}

		if (isFirstElement) {
			output = word.join('');
		} else {
			output += ` ${word.join('')}`;
		}

		isFirstElement = false;
	}

	return output;
};

s = "Let's take LeetCode contest";
console.log(reverseWords(s));
// Output: "s'teL ekat edoCteeL tsetnoc"
