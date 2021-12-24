/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
	let dp = [];
	for (let i = 0; i < triangle.length + 1; i++) {
		dp[i] = 0;
	}
	console.log(dp);
	for (let i = triangle.length - 1; i >= 0; i--) {
		console.log(triangle[i]);
		// [ 4, 1, 8, 3 ]
		for (let j = 0; j < triangle[i].length; j++) {
			// console.log(triangle[i][j]);
			dp[j] = triangle[i][j] + Math.min(dp[j], dp[j + 1]);
			console.log(dp);
		}
	}

	return dp[0];
};

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]];
// Output: 11
// Explanation: The triangle looks like:
//    2
//   3 4
//  6 5 7
// 4 1 8 3
// The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

console.log(minimumTotal(triangle));
