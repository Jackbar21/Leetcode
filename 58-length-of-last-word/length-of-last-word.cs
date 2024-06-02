public class Solution {
    public int LengthOfLastWord(string s) {
        int index = s.Length - 1;
        if (index == -1)
            return 0;
        // if (index == 0)
        //     return s[0] == ' ' ? 0 : 1;
        
        while (s[index] == ' ')
        {
            index--;
        }

        int length = 0;
        while (index >= 0 && s[index] != ' ')
        {
            index--; length++;
        }

        return length;
    }
}