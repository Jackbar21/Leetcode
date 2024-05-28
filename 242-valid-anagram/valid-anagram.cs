public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
            return false;
        
        Dictionary<char, int> ds = WordToDict(s);
        Dictionary<char, int> dt = WordToDict(t);
        foreach(char key in ds.Keys)
        {
            if (dt.ContainsKey(key) == false
                || dt[key] != ds[key])
                return false;
        }

        return true;
    }

    private Dictionary<char, int> WordToDict(string word) {
        Dictionary<char, int> result = new Dictionary<char, int>();

        foreach(char c in word)
            result[c] = result.GetValueOrDefault(c, 0) + 1;

        return result;
    }
}