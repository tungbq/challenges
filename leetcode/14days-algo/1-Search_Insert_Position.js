// Link: https://leetcode.com/problems/search-insert-position/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var searchInsert = function(nums, target) {
  let left = 0;
  let right = nums.length - 1;

  if (target < nums[left]) return left;
  if (target > nums[right]) return right + 1;

  while (left <= right) {
    let mid = Math.round((left + right ) / 2);
    console.log('mid: ', mid)

    if (target === nums[mid]) {
      return mid;
    } else if (target < nums[mid]) {
      if (target > nums[mid - 1]) {
        return mid;
      }
      right = mid - 1;
    } else {
      if (target < nums[mid+1]) {
        return mid + 1;
      }
      left = mid + 1;
    }
  }
  return -1;
};

// Expected: 4
nums = [1,3,5,6], target = 7
const result = searchInsert(nums, target)
console.log(result)
