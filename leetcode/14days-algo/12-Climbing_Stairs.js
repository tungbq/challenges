// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n, memo = {}) {
	if (n in memo) return memo[n];
	if (n === 0) return 1;
	if (n < 0) return 0;

	memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo);
	return memo[n];
};

n = 3;
// Output: 3
console.log(climbStairs(n));
