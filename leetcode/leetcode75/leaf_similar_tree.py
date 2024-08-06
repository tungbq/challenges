"""
Leaf-Similar Trees:

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1 = self._get_leaf_helper(root1, [])
        leaf2 = self._get_leaf_helper(root2, [])

        # Actually 2 leaf are diff if their length are not equal.
        if len(leaf1) != len(leaf2):
            return False

        # Now iterate the 2 arrays to check if theirs match:
        for i in range(len(leaf1)):
            if leaf1[i] is not leaf2[i]:
              # Early return if one of the leaf pair is difference!
              return False
        # If everything is OK -> just return True.
        return True

    def _get_leaf_helper(self, root: TreeNode, leafs = []):
        if not root:
            return []
        # A left will not have left and right
        if not root.left and not root.right:
            # Adding leaf node to the leafs result
            leafs.append(root.val)

        # Continue with the left and brings current leafs to the recursive function
        self._get_leaf_helper(root.left, leafs)
        # Continue with the right and brings current leafs to the recursive function
        self._get_leaf_helper(root.right, leafs)

        return leafs


# Test cases for the solution
def testLeafSimilar():
    # Test case 1: Trees with same leaf values
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)

    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.right.left = TreeNode(3)

    solution = Solution()
    assert solution.leafSimilar(root1, root2) == True, "Test case 1 failed!"

    # Test case 2: Trees with different leaf sequences
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(4)

    assert solution.leafSimilar(root1, root2) == False, "Test case 2 failed!"

    # Test case 3: One tree is empty, other is not
    root1 = None

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    assert solution.leafSimilar(root1, root2) == False, "Test case 3 failed!"

    # Test case 4: Both trees are empty
    root1 = None
    root2 = None

    assert solution.leafSimilar(root1, root2) == True, "Test case 4 failed!"

    # Test case 5: Trees with same leaves but different structure
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(4)
    root2.right = TreeNode(3)

    assert solution.leafSimilar(root1, root2) == True, "Test case 5 failed!"

    print("All test cases have passed!")

testLeafSimilar()