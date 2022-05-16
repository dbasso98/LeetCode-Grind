def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p == None and q == None:
        return True
    if (p != None and q == None) or (p == None and q != None):
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# O(n) time and space complexity.

# Pattern:
# Recursively check if the trees are equal node by node (both are leafs or have same value).
