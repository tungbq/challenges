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
		cur_node = cur_node.next;
		length += 1;
	}

	// Find index of the previous element of element to be removed
	const indexToRemove = length - n - 1;

	// Cover case remove the 'head'
	if (indexToRemove === -1) {
		head = head.next;
	} else {
		// Iterate to update linkedlist
		cur_node = head;
		let i = 0;
		while (cur_node !== null && cur_node.next !== null) {
			if (i === indexToRemove) {
				// Remove element
				cur_node.next = cur_node.next.next;
			}
			cur_node = cur_node.next;
			i++;
		}
	}
	return head;
};

// TODO: Do this in one pass...

// Input:
(head = [1, 2, 3, 4, 5]), (n = 2);
// Output: [1,2,3,5]
