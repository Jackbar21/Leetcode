class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # This is just classical sliding window
        d = {}
        l = res = cur_length = 0
        for fruit in fruits:
            d[fruit] = d.get(fruit, 0) + 1
            cur_length += 1
            while len(d) > 2:
                l_fruit = fruits[l]
                d[l_fruit] -= 1
                if d[l_fruit] == 0:
                    del d[l_fruit]
                cur_length -= 1
                l += 1
            
            if res < cur_length:
                res = cur_length
        
        return res
