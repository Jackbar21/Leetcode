class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        N = len(nums)
        hills = valleys = 0
        for i in range(1, N - 1):
            num = nums[i]
            if num == nums[i - 1]:
                continue # Discount same hill/valleys!

            found_left = found_right = False

            left_index = i - 1
            while left_index >= 0:
                if (left_num := nums[left_index]) != num:
                    found_left = True
                    break
                left_index -= 1
            if not found_left:
                continue
            
            right_index = i + 1
            while right_index < N:
                if (right_num := nums[right_index]) != num:
                    found_right = True
                    break
                right_index += 1
            if not found_right:
                continue
            
            print(f"{i=}, is_hill={left_num < num and right_num < num}, is_valley={left_num > num and right_num > num}")
            hills += left_num < num and right_num < num
            valleys += left_num > num and right_num > num
        
        return hills + valleys
