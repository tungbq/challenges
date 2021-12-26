/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
	let orangeQueue = [];

	let fresh = 0;

	row_len = grid.length;
	col_len = grid[0].length;

	for (let r = 0; r < row_len; r++) {
		for (let c = 0; c < col_len; c++) {
			if (grid[r][c] == 1) {
				fresh++;
			}
			if (grid[r][c] == 2) {
				orangeQueue.push([r, c]);
			}
		}
	}

	let time = 0;

	while (orangeQueue.length) {
		const size = orangeQueue.length;
		for (let i = 0; i < size; i++) {
			const [r, c] = orangeQueue.shift();

			if (r - 1 >= 0 && grid[r - 1][c] === 1) {
				grid[r - 1][c] = 2;
				fresh--;
				orangeQueue.push([r - 1, c]);
			}
			if (r + 1 < row_len && grid[r + 1][c] === 1) {
				grid[r + 1][c] = 2;
				fresh--;
				orangeQueue.push([r + 1, c]);
			}
			if (c - 1 >= 0 && grid[r][c - 1] === 1) {
				grid[r][c - 1] = 2;
				fresh--;
				orangeQueue.push([r, c - 1]);
			}
			if (c + 1 < col_len && grid[r][c + 1] === 1) {
				grid[r][c + 1] = 2;
				fresh--;
				orangeQueue.push([r, c + 1]);
			}
		}

		if (orangeQueue.length > 0) time++;
	}

	if (fresh == 0) {
		return time;
	} else {
		return -1;
	}
};

grid = [
	[2, 1, 1],
	[1, 1, 0],
	[0, 1, 1],
];
// Output: 4
console.log(orangesRotting(grid));

// Er 2
grid2 = [
	[2, 1, 1],
	[1, 1, 1],
	[0, 1, 2],
];
// Output: 3
console.log(orangesRotting(grid2));

// Er 3
grid3 = [[2, 2, 2, 1, 1]];
// Output: 2
console.log(orangesRotting(grid3));
