// Two Sum II - Input array is sorted
// Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let left = 0;
    let right = numbers.length - 1;

    while (left < right) {
      if ((numbers[left] + numbers[right]) < target) {
        left += 1;
      } else if ((numbers[left] + numbers[right]) > target) {
        right -= 1;
      } else {
        return [left + 1, right + 1];
      }
    }

    return [-1, -1]
};

numbers = [2,7,11,15], target = 9
console.log(twoSum(numbers, target))
// Expected output: [1,2]

numbers = [2,3,4], target = 6
console.log(twoSum(numbers, target))
// Expected output: [1,3]
