/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
	let weight = 0;
	while (n > 1) {
		if (n % 2 == 1) {
			weight += 1;
			n = n / 2 - 1;
		} else {
			n = n / 2;
		}

		console.log(n);
	}

	return weight;
};

n = 00000000000000000000000000001011;
// Output: 3
// Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

console.log(hammingWeight(n));
