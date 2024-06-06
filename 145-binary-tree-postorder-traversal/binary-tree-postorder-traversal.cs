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
    public IList<int> PostorderTraversal(TreeNode root) {
        if (root == null)
            return Enumerable.Empty<int>().ToList();

        return PostorderTraversal(root.left)
            .Concat(PostorderTraversal(root.right))
            .Append(root.val)
            .ToList();
    }
}