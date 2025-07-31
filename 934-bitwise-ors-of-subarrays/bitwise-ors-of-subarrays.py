class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        self.arr = arr
        # N = len(arr)
        # res = set()
        # # max_or = functools.reduce(lambda x, y: x | y, arr)

        # suffix_max = [] # suffix_max[i] == maximum bitwise or in arr[i:]
        # cur_bitwise_or = 0
        # for num in reversed(arr):
        #     cur_bitwise_or |= num
        #     suffix_max.append(cur_bitwise_or)
        # suffix_max = suffix_max[::-1]

        # for i, cur_num in enumerate(arr):
        #     res.add(cur_num)
        #     max_bitwise_or = suffix_max[i]
        #     for j in range(i + 1, N):
        #         cur_num |= arr[j]
        #         res.add(cur_num)
        #         if cur_num == max_bitwise_or:
        #             break
        # return len(res)
        res = set()
        for i in range(len(arr)):
            res |= self.dp(i)
        return len(res)

    # dp(i) --> set of all possible bitwise ors starting at index i
    @cache
    def dp(self, i):
        arr = self.arr
        N = len(arr)

        if i >= N:
            return set()
        
        num = arr[i]

        # Case 1: Stop at index i
        case1 = set([num])

        # Case 2: Don't stop at index i
        case2 = set(num | dp_num for dp_num in self.dp(i + 1))

        return case1 | case2
