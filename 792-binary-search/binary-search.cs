public class Solution {
    public int Search(int[] nums, int target) {
        if (nums.Length <= 0)
            return -1;
        
        if (nums.Length == 1)
            return nums[0] == target ? 0 : -1;
        
        int mid = nums.Length / 2;

        if (nums[mid] == target)
            return mid;

        if (target < nums[mid])
        {
            // Code found online for array splicing
            int start = 0;
            int end = mid - 1;
            int length = end - start + 1;
            int[] result = new int[length];
            Array.Copy(nums, start, result, 0, length);

            return Search(result, target);
        }

        // Code found online for array splicing
        int[] res = new int[nums.Length - mid - 1];
        Array.Copy(nums, mid + 1, res, 0, nums.Length - mid - 1);

        int ret = Search(res, target);
        if (ret == -1)
            return -1;

        return (mid+1) + ret;
    }
}