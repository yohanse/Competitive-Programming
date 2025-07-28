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

        def preorder(node):
            if not node:
                return "#"
            
            left = preorder(node.left)
            right = preorder(node.right)
            return f"{node.val} {left} {right}"
        
        return preorder(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split()[::-1]
        
        def preorder():

            data = arr.pop()
            if data == "#":
                return None

            node = TreeNode(data)
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))