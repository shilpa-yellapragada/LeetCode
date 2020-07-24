'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.
Eg:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        delete_set = set(to_delete)
        
        def removenodes(root, is_root):
            if not root:
                return None
            if is_root and (root.val not in delete_set):
                res.append(root)
            deleted = False
            if root.val in delete_set:
                deleted = True
            root.left = removenodes(root.left, deleted)
            root.right = removenodes(root.right, deleted)
            
            if deleted :
                return None
            else :
                return root
            
        removenodes(root,True)
        return res
        
