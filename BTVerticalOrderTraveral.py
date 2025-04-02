# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # T: O(n), S: O(n)
        if not root:
            return []

        # Dictionary to store nodes by column
        columns = defaultdict(list)

        # Queue for BFS: (node, column)
        queue = deque([(root, 0)])

        # Track min and max column to avoid sorting later
        min_col = max_col = 0

        # BFS traversal
        while queue:
            node, col = queue.popleft()

            # Add current node value to its column
            columns[col].append(node.val)

            # Update min and max column
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            # Add children to queue with their respective column positions
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        # Construct result using min_col and max_col for ordering
        result = []
        for col in range(min_col, max_col + 1):
            result.append(columns[col])

        return result
