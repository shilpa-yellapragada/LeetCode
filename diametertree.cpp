'/*
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans = 0;
    int height(TreeNode* root) {
        if(!root) {
            return 0;
        }
        int l = height(root->left);
        int r = height(root->right);
        ans = max(ans, l+r);
        return max(l,r) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        if(!root) {
            return 0;
        }
        
        int h = height(root);
        return ans;
    }
};
