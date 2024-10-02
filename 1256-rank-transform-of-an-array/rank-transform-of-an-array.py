class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) <= 0:
            return []
        sorted_arr = sorted(arr)
        d = {} # num-to-rank mappings

        # for i in range(len(arr)):
        #     rank = i + 1
        #     num = sorted_arr[i]
        #     print(rank, num, d)
        #     d[num] = min(d.get(num, rank), rank)
        # print(sorted_arr)
        # print(d)
        # return [d[num] for num in arr]
        cur_num = sorted_arr[0]
        d[sorted_arr[0]] = 1
        rank = 1
        for i in range(1, len(arr)):
            if sorted_arr[i] != sorted_arr[i - 1]:
                rank += 1
            # sorted_arr[i] = rank
            num = sorted_arr[i]
            d[num] = min(d.get(num, rank), rank)
        # print(d, arr)
        return [d[num] for num in arr]
        return sorted_arr

