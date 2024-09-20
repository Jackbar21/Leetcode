class Solution:
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def isPrefix(self, s1, s2):
        # if len(s1) != len(s2):
        #     print(f"{len(s1)=}, {len(s2)=}")
        assert len(s1) == len(s2)
        return s1 == s2
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        
        return True
        # return s1 == s2[:len(s1)+1]
    def shortestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s, 0, len(s) - 1):
            return s
        print(f"{len(s)=}")
        # return "dsadsad" if s == 'b' * len(s) else ""
        if s == "":
            return ""
        
        # Initial pivot index, as anything greater is impossible
        # Want to find largest (valid) pivot index, and return solution
        # from there.
        pivot_index = (len(s)-1)//2
        
        string_to_match = collections.deque(s[pivot_index + 1:]) # always append-left pivot index
        match_copy = string_to_match.copy()
        cur = collections.deque(s[:pivot_index][::-1]) # backwards
        #print(pivot_index, cur, string_to_match)
        # return ""
        while len(match_copy) > len(cur):
            match_copy.pop()
        # while not self.isPrefix(cur, string_to_match):
        while not self.isPrefix(cur, match_copy):
            letter = cur.popleft()
            # if letter == s[pivot_index] and self.isPrefix(cur, string_to_match):
            tmp = match_copy.pop()
            if letter == s[pivot_index] and self.isPrefix(cur, match_copy):
                #print("CASEEEE")
                return ''.join(list(string_to_match)[::-1]) + letter*2 + ''.join(string_to_match)
            match_copy.append(tmp)
            # break
            string_to_match.appendleft(s[pivot_index])
            match_copy.appendleft(s[pivot_index])

            # make match_copy same in length as cur
            # they used to be same, we -1 in cur, +1 in match_copy,
            # so now just -2 in match_copy to make them even :)
            for i in range(2):
                match_copy.pop()
            
            # assert cur.popleft() == s[pivot_index - 1]
            # #print(cur.popleft(), s[pivot_index])

            pivot_index -= 1
            #print(pivot_index, cur, string_to_match)
        
        #print(f"Final pivot index: {pivot_index}")
        string = ''.join(string_to_match)
        # res = ''.join([string[::-1], string])
        # if len(cur) == 0 and not len(string) % 2 and self.isPalindrome(res, 0, len(res) - 1):
        #     return res
        # if len(cur) == 0 and len(string) % 2 == 0:
        #     # string_to_match = list(string_to_match)[1:]
        #     # pivot_index = 0
        #     return ''.join([string[::-1], string])
        # #print(string_to_match)
        # return ''.join(list(string_to_match)[::-1]) + s[pivot_index] + ''.join(string_to_match)
        
        return ''.join([string[::-1], s[pivot_index], string])

        # if self.isPalindrome(s, 0, len(s) - 1):
        #     return s
        
        # res = collections.deque([letter for letter in s])
        # for i in range(1, len(s) - 0):
        #     # res = s[-i:][::-1] + s
        #     res.append(s[-i])
        #     #print(res)
        #     i, j = 0, len(res) - 1
        #     if self.isPalindrome(res, i, j):
        #         return ''.join(res)
        # return ""

# 7 --> index 3
# 6 --> index 2
# 5 --> index 2

# pivot_index = (len(s)-1)//2
# string_to_match = collections.deque(s[pivot_index + 1:]) # always append-left pivot index

# aPbcd
# if to left of pivot as a PREFIX of string-to-match, then string-to-match[::-1], 

# abbPacd

# aPacd