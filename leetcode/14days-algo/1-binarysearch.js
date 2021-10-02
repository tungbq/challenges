/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var search = function(nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.round((left + right ) / 2);
    if (target === nums[mid]) {
      return mid;
    } else if (target < nums[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return -1;
}

// Expected: 4
nums = [-1,0,3,5,9,12], target = 9

const result = search(nums, target)
console.log('Result: ' + result)
