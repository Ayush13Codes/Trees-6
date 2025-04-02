# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # T: O(n), S: O(n)
        # Helper function for preorder traversal
        def preorder(node):
            if not node:
                vals.append("None")  # Marker for null nodes
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        vals = []
        preorder(root)
        return ",".join(vals)  # Use comma as delimiter

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # T: O(n), S: O(n)
        # Helper function to build tree from preorder sequence
        def build_tree():
            val = next(vals)
            if val == "None":
                return None

            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node

        vals = iter(data.split(","))
        return build_tree()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
