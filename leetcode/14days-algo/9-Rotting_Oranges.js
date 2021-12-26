/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
	const orangeQueue = [];

	let time = 0;
	let fresh = 0;

	row_len = grid.length;
	col_len = grid[0].length;

	for (let r = 0; r < row_len; r++) {
		for (let c = 0; c < col_len; c++) {
			if (grid[r][c] == 1) {
				fresh += 1;
			}
			if (grid[r][c] == 2) {
				orangeQueue.push([r, c]);
			}
		}
	}

	dirs = [
		[0, 1],
		[0, -1],
		[1, 0],
		[-1, 0],
	];

	while (orangeQueue.length && fresh > 0) {
		for (let i = 0; i < [...orangeQueue].length; i++) {
			const r_c = orangeQueue.shift();

			let r = r_c[0];
			let c = r_c[1];
			for (let dr = 0; dr < dirs.length; dr++) {
				let row = dirs[dr][0] + r;
				let col = dirs[dr][1] + c;

				if (
					row < 0 ||
					row >= row_len ||
					col < 0 ||
					col >= col_len ||
					grid[row][col] != 1
				) {
					continue;
				}

				// if in bounds and fresh, make it rotten
				grid[row][col] = 2;

				// Dequeue implementation in a simple way: https://stackoverflow.com/a/63466175
				orangeQueue.push([row, col]);
				fresh -= 1;
			}
		}

		time += 1;
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

// Ex 2
grid2 = [
	[2, 1, 1],
	[1, 1, 1],
	[0, 1, 2],
];
// Output: 3
console.log(orangesRotting(grid2));

// Ex 3
grid3 = [[2, 2, 2, 1, 1]];
// Output: 2
console.log(orangesRotting(grid3));
