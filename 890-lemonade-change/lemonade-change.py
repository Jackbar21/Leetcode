class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {
            5: 0,
            10: 0,
            20: 0
        }

        for bill in bills:
            assert bill in [5, 10, 20]

            # Case 1: customer pays $5, do nothing!
            if bill == 5:
                change[5] += 1
            
            # Case 2: customer pays $10, check if have $5 to give back!
            elif bill == 10:
                change[10] += 1
                if change[5] > 0:
                    change[5] -= 1  
                else:
                    assert change[5] == 0
                    return False
            
            # Case 3: customer pays $20, check if can give back $10 + $5 or 3 x $5
            else:
                assert bill == 20
                change[20] += 1
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
        
        return True