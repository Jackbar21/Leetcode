class Solution:
    def minLength(self, s: str) -> int:
        # arr = collections.deque(['dummy'])
        arr = ['dummy']

        for char in s:
            if char not in "BD":
                arr.append(char)
                continue
            
            if char == "B":
                if arr[-1] == "A":
                    arr.pop()
                else:
                    arr.append(char)
            
            if char == "D":
                if arr[-1] == "C":
                    arr.pop()
                else:
                    arr.append(char)
        
        return len(arr) - 1

        # for char in s:
        i = 0
        while i < len(s):
            char = s[i]
            if char not in "AC":
                arr.append(char)
                i += 1
                continue
            
            if char == "A":
                count_a = 0
                while i < len(s) and s[i] == "A":
                    i += 1
                    count_a += 1
                if i >= len(s):
                    break
                while i < len(s) and char in "AB":
                    char = s[i]
                    if char == "A":
                        count_a += 1
                    else:
                        count_b += 1

                    i += 1

        return len(arr) - 1
