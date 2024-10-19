class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        arr = [0]
        while k > len(arr):
            arr.append(1)
            arr.extend(1 - arr[i] for i in range(len(arr) - 2, -1, -1))
        return str(arr[k - 1])