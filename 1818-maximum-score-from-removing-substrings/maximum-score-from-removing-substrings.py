class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if x > y:
            (count, new_s) = self.removeAllSubstrings(s, "ab")
            res += x * count
            res += y * self.removeAllSubstrings(new_s, "ba")[0]
        else:
            (count, new_s) = self.removeAllSubstrings(s, "ba")
            res += y * count
            res += x * self.removeAllSubstrings(new_s, "ab")[0]
        
        return res

    def removeAllSubstrings(self, s, sub):
        # removes all occurrances of 'sub' in 's'
        # returns two-item tuple with:
        #    (1) count of all removed occurrances
        #    (2) updated string s itself
        new_s = []
        count = 0

        for char in s:
            new_s.append(char)
            if len(new_s) >= len(sub) and ''.join(new_s[-len(sub):]) == sub:
                count += 1
                for _ in range(len(sub)):
                    new_s.pop()
        
        return count, ''.join(new_s)