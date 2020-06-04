// Time: O(n)
// Space: O(logn) 
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return balancedHeight(root) >= 0;
    }
private:
    int balancedHeight(TreeNode* root) {
        if (root == nullptr) return 0;

        int left = balancedHeight(root->left);
        int right = balancedHeight(root->right);

        if (left < 0 || right < 0 || abs(left - right) > 1) return -1;

        return max(left, right) + 1;
    }
};