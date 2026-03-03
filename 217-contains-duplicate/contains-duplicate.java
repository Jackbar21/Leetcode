class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet hs = new HashSet();

        for (int i = 0; i < nums.length; i++)
        {
            int num = nums[i];
            if (hs.contains(num))
            {
                return true;
            }

            hs.add(num);
        }

        return false;
    }
}