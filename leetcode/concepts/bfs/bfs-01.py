from collections import deque

# Define the Node class for the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Breadth-First Search function
def bfs(root):
    if not root:
        return []
    
    # Initialize a queue using deque for efficient pop from the front
    queue = deque([root])
    # List to store the order of visited nodes
    result = []
    
    while queue:
        # Pop the node from the front of the queue
        current_node = queue.popleft()
        # Append the current node's value to the result list
        result.append(current_node.value)
        
        # If the current node has a left child, add it to the queue
        if current_node.left:
            queue.append(current_node.left)
        
        # If the current node has a right child, add it to the queue
        if current_node.right:
            queue.append(current_node.right)
    
    return result

# Example usage:
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    # Perform BFS on the binary tree
    print("Breadth-First Search result:", bfs(root))
