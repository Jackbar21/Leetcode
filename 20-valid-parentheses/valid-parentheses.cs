public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> closed_to_open = new Dictionary<char, char>();
        closed_to_open.Add(')', '(');
        closed_to_open.Add('}', '{');
        closed_to_open.Add(']', '[');

        Stack<char> stack = new Stack<char>();

        for (int i = 0; i < s.Length; i++)
        {
            char parenthese = s[i];

            if (closed_to_open.ContainsKey(parenthese))
            {
                // Closed parenthese
                if (stack.Count == 0)
                    return false;
                
                char innermost_parenthese = stack.Pop();
                if (closed_to_open[parenthese] != innermost_parenthese)
                    return false;
            }
            else
            {
                // Open parenthese
                stack.Push(parenthese);
            }
        }

        return stack.Count == 0;
    }
}