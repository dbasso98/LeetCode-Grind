def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return
    root.left, root.right=invertTree(root.right),invertTree(root.left)
    return root

# O(n) time and space complexity.

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            stack.extend([node.left,node.right])
            node.left, node.right = node.right, node.left
    return root

# Pattern:
# Using recursion we just have to swap the node to call to invert the tree.
# Iteratively we can use a stack to store child nodes of the current one and swap them.
