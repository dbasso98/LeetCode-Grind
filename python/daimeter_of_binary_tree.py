def compute_height(self, root):
    if not root:
        return 0
    left_height = self.compute_height(root.left)
    right_height = self.compute_height(root.right)
    self.diameter = max(self.diameter, right_height+left_height)
    return max(right_height, left_height) + 1
        
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.diameter = 0
    self.compute_height(root)
    return self.diameter

# O(n) time complexity and O(n) space.

# Pattern:
# Just compute max height of both right and left root subtree and sum them.
