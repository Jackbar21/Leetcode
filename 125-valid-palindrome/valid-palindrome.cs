public class Solution {
    public bool IsPalindrome(string s) {
        if (s.Length <= 1)
            return true;
        
        return IsPalindromeRec(s, 0, s.Length - 1);
    }

    private bool IsPalindromeRec(string s, int left, int right)
    {
        if (left >= right)
            return true;

        // Console.WriteLine($"s: \"{s}\", left: {left}, right: {right}");

        while (left < right && !char.IsLetterOrDigit(s[left]))
            left++;
        while (left < right && !char.IsLetterOrDigit(s[right]))
            right--;
        
        // if (left >= right)
        //     return true;

        if (char.ToLower(s[left]) != char.ToLower(s[right]))
            return false;
        
        // if (left + 1 >= right - 1)
        //     return true;
        
        return IsPalindromeRec(s, left + 1, right - 1);
    }
}