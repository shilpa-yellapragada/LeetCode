'''
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        def flat(root):
            p = root
            q = None
            nxt = p
            while p:
                #print(p.val)
                nxt = p.next
                if p.child:
                    last = flat(p.child)
                    #print(last.val)
                    p.next = p.child
                    p.child.prev = p
                    last.next = nxt
                    if nxt:
                        nxt.prev = last
                    p.child = None
                    nxt = p.next
                q = p
                p = nxt
                
            return q
