/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private int globalSum;
    public TreeNode BstToGst(TreeNode root) {
        this.globalSum = BstGetSum(root);
        return BstToGstAcc(root);
    }

    private TreeNode BstToGstAcc(TreeNode root)
    {
        if (root == null)
            return root;

        BstToGstAcc(root.left);

        // inorder traversal logic here
        this.globalSum -= root.val;
        root.val += this.globalSum;

        BstToGstAcc(root.right);
        
        return root;
    }

    private int BstGetSum(TreeNode root)
    {
        return (root == null) ? 0 : root.val + BstGetSum(root.left) + BstGetSum(root.right);
    }
}