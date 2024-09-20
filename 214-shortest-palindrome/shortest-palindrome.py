class Solution:
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def shortestPalindrome(self, s: str) -> str:
        # Base Case: s is already a palindrome!
        if s == "" or self.isPalindrome(s, 0, len(s) - 1):
            return s
        
        # Initial pivot index, as anything greater is impossible
        # Want to find largest (valid) pivot index, and return solution
        # from there.
        pivot_index = (len(s)-1)//2
        
        string_to_match = collections.deque(s[pivot_index + 1:]) # always append-left pivot index
        match_copy = string_to_match.copy() # dynamic copy of string_to_match, used for checking
        cur = collections.deque(s[:pivot_index][::-1]) # backwards

        while len(match_copy) > len(cur):
            match_copy.pop()
        while cur != match_copy:
            letter = cur.popleft()
            tmp = match_copy.pop()
            if letter == s[pivot_index] and cur == match_copy:
                return ''.join(list(string_to_match)[::-1]) + letter*2 + ''.join(string_to_match)
            match_copy.append(tmp)

            # Loop Invariant (in addition to cur.popleft())
            string_to_match.appendleft(s[pivot_index])
            match_copy.appendleft(s[pivot_index])
            pivot_index -= 1

            # mMke match_copy same in length as cur
            # they used to be same, we -1 in cur, +1 in match_copy,
            # so now just -2 in match_copy to make them even :)
            match_copy.pop()
            match_copy.pop()

        string = ''.join(string_to_match)
        return ''.join([string[::-1], s[pivot_index], string])