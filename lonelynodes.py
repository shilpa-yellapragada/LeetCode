'''
In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        def dfs(root):
            if not root:
                return 

            if root.left and not root.right:
                ans.append(root.left.val)

            if root.right and not root.left:
                ans.append(root.right.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)  
        return ans
