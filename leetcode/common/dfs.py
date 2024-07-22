# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


# Recursive approach
def depth_first_search(node):
    if not node:
        return
    print(node.val)  # Process the node
    depth_first_search(node.left)
    depth_first_search(node.right)

# Example usage:
root_list = [3, 9, 20, None, None, 15, 7]
root = list_to_tree(root_list)
depth_first_search(root)
