public class Solution {
    public int LengthOfLongestSubstring(string s) {
        HashSet<char> hs = new HashSet<char>();
        int l = 0;
        int longest = 0;
        int res = 0;

        for (int i = 0; i < s.Length; i++)
        {
            char letter = s[i];
            while (hs.Contains(letter))
            {
                hs.Remove(s[l]);
                l += 1;
            }

            hs.Add(letter);
            if (i - l + 1 > res)
                res = i - l + 1;
        }

        return res;
    }
}