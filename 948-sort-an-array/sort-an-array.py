class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums)-1)
    def mergeSort(self, nums, left, right):
        if left >= right:
            return [nums[left]] if left == right else []
        mid = (right+left) // 2
        
        left_arr = self.mergeSort(nums, left, mid)
        right_arr = self.mergeSort(nums, mid+1, right)

        l,r = 0,0
        res = []
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                res.append(left_arr[l])
                l += 1
            else:
                res.append(right_arr[r])
                r += 1
        
        if l >= len(left_arr):
            res += right_arr[r:]
        else:
            res += left_arr[l:]
        
        return res