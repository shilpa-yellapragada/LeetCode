'''
You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
'''

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        def dll(root):
            if root == None:
                return None, None
            
            l1, h1 = dll(root.left)
            l2, h2 = dll(root.right)
            
            root.left = h1
            root.right = l2
            
            if h1:
                h1.right = root
            if l2:
                l2.left = root
            
            if not l1:
                l1 = root
            if not h2:
                h2 = root
                
            return l1, h2
        
        if not root:
            return None
        
        x, y = dll(root)
        
        if not x:
            x = root
        if not y:
            y = root
            
        y.right = x
        x.left = y
        
        return x
        
        
