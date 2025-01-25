class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        d = {}

        i = 0
        while i < N:
            # Create new connected component
            num, num_index = sorted_nums[i]
            upper_bound = num + limit
            i += 1
            connected_component = [num]
            d[num_index] = connected_component
            while i < N:
                sorted_num, sorted_index = sorted_nums[i]

                # Break if doesn't belong to same connected component!
                if sorted_num > upper_bound:
                    break

                # Update upper_bound
                upper_bound = sorted_num + limit
    
                connected_component.append(sorted_num)
                d[sorted_index] = d[num_index]
                i += 1
            
            connected_component.reverse() # Since can only pop() in arrays, and will need smallest values!
        
        return [d[i].pop() for i in range(N)]
