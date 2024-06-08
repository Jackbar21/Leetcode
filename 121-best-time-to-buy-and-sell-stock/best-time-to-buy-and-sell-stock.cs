public class Solution {
    public int MaxProfit(int[] prices) {
        int left = 0, right = 0, curMax = 0;
        while (right < prices.Length){
            if (prices[right] < prices[left])
                left = right;
            if (curMax < prices[right] - prices[left])
                curMax = prices[right] - prices[left];

            // Loop Invariant
            right += 1;
        }

        return curMax;
    }
}