def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	def search(root, node, parent_list = []):
		if root is None:
			return parent_list
		parent_list.append(root)
		if root.val > node.val:
			return search(root.left, node, parent_list)
		elif root.val < node.val:
			return search(root.right, node, parent_list)
		else:
			return parent_list
	parents_p, parents_q = search(root, p, []), search(root, q, [])
	for pointer in range(min(len(parents_p), len(parents_q))):
		if parents_p[pointer] == parents_q[pointer]:
			lowest_common_ancestor = parents_p[pointer]

	return lowest_common_ancestor

# O(n) for both space and time complexity.
# To reduce space complexity to O(1) we can go for the iterative solution:

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	while True:
		if root.val < p.val and root.val < q.val:
			root = root.right
		elif root.val > p.val and root.val > q.val:
			root = root.left
		else:
			return root

# Pattern:
# Thinking about the problem, if both elements are smaller or larger than the 
# root then this means that they are both located in the same subtree. 
# As soon as this doesn’t hold true then we’ve found the LCA.
