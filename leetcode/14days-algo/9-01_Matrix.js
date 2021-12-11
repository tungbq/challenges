/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function (mat) {
	for (let i = 0; i < mat.length; i++) {
		for (let j = 0; j < mat.length; j++) {
			if (mat[i][j] == 1) {
				mat[i][j] = dfs(mat, i, j);
			}
		}
	}
	return mat;
};

var dfs = function (mat, i, j) {
	let minLength = 1;
	if (i < 0 || i >= mat.length || j < 0 || j >= mat[i].length || ) {
		return minLength;
	}

  minLength = Math.min(minLength, dfs(mat, i-1, j));
  minLength = Math.min(minLength, dfs(mat, i+1, j));
  minLength = Math.min(minLength, dfs(mat, i, j-1));
  minLength = Math.min(minLength, dfs(mat, i, j+1));

  return minLength
};

mat = [
	[0, 0, 0],
	[0, 1, 0],
	[1, 1, 1],
];
// Output: [[0,0,0],[0,1,0],[1,2,1]]

console.log(updateMatrix(mat));
