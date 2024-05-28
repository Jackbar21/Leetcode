public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int left = 0, right = numbers.Length - 1;

        while (numbers[left] + numbers[right] != target)
        {
            if (numbers[left] + numbers[right] > target)
                right--;
            else
                left++;
        }

        // Return the indices of the two numbers, index1 and index2, 
        // added by one as an integer array [index1, index2] 
        // of length 2.
        left++; right++;
        return left < right ? new int[] {left, right} : new int[] {right, left};
    }
}