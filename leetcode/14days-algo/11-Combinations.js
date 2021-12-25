/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
	if (n == 1 && k == 1) return [[1]];
	let answers = [];
	const comb = (set, startNumber, answers) => {
		if (set.length == k) answers.push(Array.from(set));
		for (let i = startNumber; i <= n; i++) {
			set.push(i);
			comb(set, i + 1, answers);
			set.pop();
		}
	};
	comb([], 1, answers);
	return answers;
};

(n = 4), (k = 2);

console.log(combine(n, k));
// answersput:
// [
//   [2,4],
//   [3,4],
//   [2,3],
//   [1,2],
//   [1,3],
//   [1,4],
// ]
