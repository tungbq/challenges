// Breadth-First Search / Depth-First Search

// Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
// The distance between two adjacent cells is 1.

/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function (mat) {
	let results = [];
	let visited = [];

	// Create a 2-d array to keep track visited
	for (let i = 0; i < mat.length; i++) {
		let row_visited = [];
		for (let j = 0; j < mat[i].length; j++) {
			row_visited.push(false);
		}
		visited.push(row_visited);
	}

	for (let i = 0; i < mat.length; i++) {
		let row_result = [];
		for (let j = 0; j < mat[i].length; j++) {
			if (mat[i][j] === 1) {
				let nearestLen = dfs(mat, i, j, visited);
				row_result.push(nearestLen);
			} else {
				results.push(0);
			}
		}
		results.push(row_result);
	}

	return results;
};

var dfs = function (mat, i, j, visited = []) {
	if (
		i < 0 ||
		i >= mat.length ||
		j < 0 ||
		j >= mat[i].length ||
		visited[i][j]
	) {
		return 100000;
	}

	if (mat[i][j] === 0) {
		return 0;
	}

	visited[i][j] = true;
	let nearestZero =
		1 +
		Math.min(
			dfs(mat, i + 1, j, visited),
			dfs(mat, i - 1, j, visited),
			dfs(mat, i, j + 1, visited),
			dfs(mat, i, j - 1, visited)
		);

	visited[i][j] = false;
	return nearestZero;
};

mat = [
	[0, 0, 0],
	[0, 1, 0],
	[1, 1, 1],
];
// Output: [[0,0,0],[0,1,0],[1,2,1]]
console.log(updateMatrix(mat));
