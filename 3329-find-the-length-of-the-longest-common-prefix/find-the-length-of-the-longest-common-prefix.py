class Solution:
    def __init__(self):
        self.trie1 = {}
        self.trie2 = {}
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = set(str(num) for num in arr1)
        arr2 = set(str(num) for num in arr2)

        # Idea: add every number to a trie, each number being at most 9 characters in length
        # and there are at most 2 * (5 * 10^4) == 10^5 elements. 9 * 10^5 < 10^6, which is
        # acceptable number of "iterations" supported for a solution on leetcode. Then we do
        # same thing to get longest prefix, i.e. get length of each number in the trie, which
        # we now know has a max depth of 9, so will take an additional < 10^5 number of
        # "iterations", which again, is also fine. 2 * 10^6 is reasonable on Leetcode.

        # Step 1: Add every number to trie
        for str_num in arr1:
            self.insertNum(self.trie1, str_num)
        for str_num in arr2:
            self.insertNum(self.trie2, str_num)
        
        print(self.trie1)
        print(self.trie2)
        
        # Step 2: For each num in arr1, get longest prefix in trie2.
        #         For each num in arr2, get longest prefix in trie1.
        res = 0
        for str_num in arr1:
            res = max(res, self.getPrefixLength(self.trie2, str_num))
        for str_num in arr2:
            res = max(res, self.getPrefixLength(self.trie1, str_num))

        return res
    
    def insertNum(self, trie, str_num):
        for digit in str_num:
            if digit not in trie:
                trie[digit] = {}
            trie = trie[digit]
    
    def getPrefixLength(self, trie, str_num):
        res = 0
        for digit in str_num:
            if digit not in trie:
                break
            res += 1
            trie = trie[digit]
        return res