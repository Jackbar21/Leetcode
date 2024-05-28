public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        /*
         * Want to keep track of nums we've already seen.
         * For each num we traverse, we want to check if
         * we've already found another number such that:
         *      num + other_num = target
         *  ==> other_num = target - num
         * 
         * So at any point, when traversing nums, we check
         * that we've already previously found a number whose
         * value is (target - num), we have found our solution.
         */

         Dictionary<int, int> seen = new Dictionary<int, int>();

         for (int i = 0; i < nums.Length; i++)
         {
            int num = nums[i];
            int wanted_num = target - num;

            if (seen.ContainsKey(wanted_num))
            {
                int prev_index = seen[wanted_num];
                return new int[] {prev_index, i};
            }

            // seen.Add(num, i);
            seen[num] = i;
         }

         throw new Exception("Error: Should not reach here.");
    }
}