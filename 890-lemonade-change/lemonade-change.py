class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bills, ten_bills = 0, 0

        for bill in bills:
            # Case 1: customer pays $5, do nothing!
            if bill == 5:
                five_bills += 1
            
            # Case 2: customer pays $10, check if have $5 to give back!
            elif bill == 10:
                ten_bills += 1
                if five_bills > 0:
                    five_bills -= 1
                else:
                    return False
            
            # Case 3: customer pays $20, check if can give back $10 + $5 or 3 x $5
            else:
                if ten_bills > 0 and five_bills > 0:
                    ten_bills -= 1
                    five_bills -= 1
                elif five_bills >= 3:
                    five_bills -= 3
                else:
                    return False
        
        # Broke exact change for every customer, so return true!
        return True