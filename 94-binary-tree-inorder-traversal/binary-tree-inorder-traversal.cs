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
    public IList<int> InorderTraversal(TreeNode root) {
        // List<int> res = new List<int>();
        if (root == null)
            return new List<int>();
        
        List<int> left = (List<int>)InorderTraversal(root.left);
        left.Add(root.val);
        List<int> right = (List<int>)InorderTraversal(root.right);
        foreach (int val in right)
            left.Add(val);
        return left;
    }
}