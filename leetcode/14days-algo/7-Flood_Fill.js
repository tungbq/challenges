/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, newColor) {
	if (image[sr][sc] === newColor) {
		return image;
	}

	const source = image[sr][sc];
	const rows = image.length;
	const cols = image[0].length;

	dfs(image, sr, sc, newColor, rows, cols, source);
	return image;
};

const dfs = function (image, sr, sc, newColor, rows, cols, source) {
	// Base case for recursuve function:
	if (sr < 0 || sr >= rows || sc < 0 || sc >= cols) {
		return;
	}

	if (image[sr][sc] !== source) {
		return;
	}

	// Update color
	image[sr][sc] = newColor;

	// Recursive on 4-directionally:
	dfs(image, sr - 1, sc, newColor, rows, cols, source); // TOP
	dfs(image, sr, sc + 1, newColor, rows, cols, source); // RIGHT
	dfs(image, sr + 1, sc, newColor, rows, cols, source); // BOTTOM
	dfs(image, sr, sc - 1, newColor, rows, cols, source); // LEFT
};

// Input:
(image = [
	[1, 1, 1],
	[1, 1, 0],
	[1, 0, 1],
]),
	(sr = 1),
	(sc = 1),
	(newColor = 2);

(image = [
	[0, 0, 0],
	[0, 0, 0],
]),
	(sr = 0),
	(sc = 0),
	(newColor = 2);

// Expected Output: [[2,2,2],[2,2,0],[2,0,1]]

console.log(floodFill(image, sr, sc, newColor));

// Time: O(m*n), Space: O(1)
