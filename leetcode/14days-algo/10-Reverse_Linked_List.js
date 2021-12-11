/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseList = function(head) {
  let prev = null;
  
  while (head !== null) {
      let next_node = head.next;
      head.next = prev;
      prev = head;
      head = next_node;
  }
  
  return prev;
};

// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]