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
        new_s = []
        count = 0
        sub_len = len(sub)

        for char in s:
            new_s.append(char)
            if len(new_s) >= sub_len and ''.join(new_s[-sub_len:]) == sub:
                count += 1
                del new_s[-sub_len:]
        
        return count, ''.join(new_s)
        # removes all occurrances of 'sub' in 's'
        # returns two-item tuple with:
        #    (1) count of all removed occurrances
        #    (2) updated string s itself
        # Prerequisite: 'sub' must be of length 2

        new_s = [s[0]]
        count = 0

        prev = s[0]
        for i in range(1,len(s)):
            cur = s[i]

            if prev + cur == sub:
                count += 1
                new_s.pop()
            else:
                new_s.append(cur)
            
            prev = cur
        
        return (count, ''.join(new_s))


