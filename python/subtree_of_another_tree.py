class Solution:
    def isIdentical(self, root, subRoot):
        if root and subRoot:
            return root.val == subRoot.val and self.isIdentical(root.left, subRoot.left) and self.isIdentical(root.right, subRoot.right)
        return root is subRoot
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root :
            return False
        if self.isIdentical(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

# Pattern:
# Check for matching subtrees recursively in the usual way. But, first find the root of the subtree in the main tree (if it exists).
