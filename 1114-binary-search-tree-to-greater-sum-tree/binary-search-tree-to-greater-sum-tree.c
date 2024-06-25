/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int globalSum;
int bstGetSum(struct TreeNode* root)
{
    return (root == NULL) ? 0 : root->val + bstGetSum(root->left) + bstGetSum(root->right);
}

struct TreeNode* bstToGstAcc(struct TreeNode* root)
{
    if (root == NULL)
        return root;
    
    // inorder
    root->left = bstToGstAcc(root->left);

    globalSum -= root->val;
    root->val += globalSum;

    root->right = bstToGstAcc(root->right);

    return root;
}

struct TreeNode* bstToGst(struct TreeNode* root) {
    globalSum = bstGetSum(root);
    return bstToGstAcc(root);
}



