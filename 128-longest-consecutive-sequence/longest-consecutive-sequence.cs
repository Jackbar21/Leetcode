public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> hs = new HashSet<int>();
        int res = 0;
        foreach (int num in nums)
            hs.Add(num);
        
        foreach (int num in nums)
        {
            if (!hs.Contains(num - 1))
            {
                int length = 0;
                while (hs.Contains(num + length))
                    length += 1;
                
                if (length > res)
                    res = length;
            }
        }

        return res;
    }
}