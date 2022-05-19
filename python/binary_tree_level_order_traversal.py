import collections

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    queue = collections.deque()
    result = []
    if not root:
        return []
    else:
        queue.append(root)
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

# Time complexity is O(n) and space complexity is O(n) since we are going to add 
# at most all the elements to the queue.

# Pattern:
# Use BFS to traverse the binary tree properly. Pay attention to how store at the correct level the nodes.
