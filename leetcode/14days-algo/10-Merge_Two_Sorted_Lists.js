* Definition for singly-linked list.
* function ListNode(val, next) {
*     this.val = (val===undefined ? 0 : val)
*     this.next = (next===undefined ? null : next)
* }
*/
/**
* @param {ListNode} list1
* @param {ListNode} list2
* @return {ListNode}
*/
var mergeTwoLists = function (list1, list2) {
   let temp_node = new ListNode(0);
   let current_node = temp_node;

   while (list1 !== null && list2 !== null) {
       if (list1.val < list2.val) {
           current_node.next = list1;
           list1 = list1.next;
       } else {
           current_node.next = list2;
           list2 = list2.next;
       }
       
       current_node = current_node.next;
   }

 if (list1 !== null) {
   current_node.next = list1;
   list1 = list1.next;
 }

 if (list2 !== null) {
   current_node.next = list2;
   list2 = list2.next;
 }

 return temp_node.next;
};

(list1 = [1, 2, 4]), (list2 = [1, 3, 4]);
// Output: [1,1,2,3,4,4]
