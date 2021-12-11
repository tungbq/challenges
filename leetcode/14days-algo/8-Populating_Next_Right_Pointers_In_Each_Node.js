/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
 var connect = function (root) {
	if (root == null) {
		return root;
	}

	var leftNode = root;

	while (leftNode && leftNode.left != null) {
		var head = leftNode;

		while (head != null) {
			head.left.next = head.right;
			if (head.next != null) {
				head.right.next = head.next.left;
			}
			head = head.next;
		}

		leftNode = leftNode.left;
	}

	return root;
};

root = [1,2,3,4,5,6,7]
// Output: [1,#,2,3,#,4,5,6,7,#]
