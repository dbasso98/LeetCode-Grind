class Solution:
    def __init__(self):
        self.register = {}
        
    def compute_height(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return 0
        if root in self.register:
            return self.register[root]
        else:
            self.register[root] = max(self.compute_height(root.left), self.compute_height(root.right)) + 1
            return self.register[root]
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left_height = self.compute_height(root.left)
        right_height = self.compute_height(root.right)
        return abs(left_height-right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# Pattern:
# Faster solution using memoization. We can recall previously obtained results because we 
# have to check the balancing property for every node in the tree.
