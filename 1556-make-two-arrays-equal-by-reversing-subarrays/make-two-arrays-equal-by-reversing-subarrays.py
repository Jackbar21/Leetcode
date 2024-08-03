class Solution:
    def convertArrToDict(self, arr):
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1
        return d
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # 1,2,3
        target_dict = self.convertArrToDict(target)
        arr_dict = self.convertArrToDict(arr)
        return target_dict == arr_dict

        # 1,2,3 YES
        # 1,3,2 YES
        # 2,3,1 YES
        # 2,1,3 YES
        # 3,1,2 YES 
        # 3,2,1 YES

        # for 0 <= n <= 3
        # reversing subarrays means u can reach every permutation

        # WTS: can reach every permutation for i + 1 given u can for i
