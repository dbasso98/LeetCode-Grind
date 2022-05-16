def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    return max(left_depth, right_depth) + 1

# O(n) time and space complexity.

# Pattern:
# Recursively traverse the tree by looking at left and right subtree. DFS!
