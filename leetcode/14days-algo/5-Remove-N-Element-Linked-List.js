// Remove Nth Node From End of List

// Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Follow up: Could you do this in one pass?

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
	// Calculate length of list
	let cur_node = head;
	let length = 1;
	while (cur_node.next !== null) {
		length += 1;
	}

	// Find index of element to remove
	const indexToRemove = length - n - 1;

	// Iterate to update linkedlist
	cur_node = head;
	for (let i = 0; i < length; i++) {
		if (i === indexToRemove) {
			// Remove next element
			cur_node.next = cur_node.next.next;
		}
		cur_node = cur_node.next;
	}
};

// TODO: Do this in one pass...

// Input:
(head = [1, 2, 3, 4, 5]), (n = 2);
// Output: [1,2,3,5]
