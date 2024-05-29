public class Solution {
    public bool IsHappy(int n) {
        HashSet<int> seen = new HashSet<int>();

        int num = n;
        while (!seen.Contains(num))
        {
            seen.Add(num);

            num = num.ToString().Sum(c => (int)Math.Pow(c - '0', 2));
            if (num == 1)
                return true;
        }

        return false;
    }
}