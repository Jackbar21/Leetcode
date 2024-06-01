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
    public TreeNode SortedArrayToBST(int[] nums) {
        if (nums.Length == 0)
            return null;
        
        int mid = nums.Length / 2; // Rounds down
        int[] left = nums.Skip(0).Take(mid).ToArray();
        int[] right = nums.Skip(mid + 1).Take(nums.Length - mid - 1).ToArray();

        TreeNode root = new TreeNode(nums[mid]);
        root.left = SortedArrayToBST(left);
        root.right = SortedArrayToBST(right);

        return root;
    }
}