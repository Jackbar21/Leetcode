class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1, nums2 = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        N, M = len(nums1), len(nums2)

        # Returns how many products are <= 'product' from nums1 & nums2 possible pairs
        def getProductCount(product): # O(NlogM)
            res = 0
            for num1 in nums1:
                # want num1 * num2 <= product
                # <--> num2 <= product / num1
                #      IF num1 is POSITIVE, ELSE
                #      num2 >= product / num1

                # Handle num1 == 0 case since division by zero not allowed!
                if num1 == 0:
                    res += M if product >= 0 else 0
                    continue
                
                threshold = product / num1

                # If num1 is positive, then:
                # Find largest (i.e. rightmost) valid element in nums2 
                if num1 > 0:
                    l, r = 0, M - 1
                    while l <= r:
                        mid = (l + r) // 2
                        num2 = nums2[mid]
                        if num2 <= threshold:
                            # Valid solution, look for even more valid rightmost ones
                            l = mid + 1
                        else:
                            # Invalid solution, look for valid ones on left
                            r = mid - 1
                    
                    # Every product between num1 and any number in nums2[0..rightmost]
                    # is valid. Hence, there are rightmost + 1 total valid products
                    res += r + 1
                    continue

                # assert num1 < 0
                # num1 is negative, and we still want to find number of products.
                # This means the solutions are gonna lie on RIGHT side of array!
                # So want to find leftmost index where num1 * num2 <= product,
                # and count numbers from nums2[leftmost..M-1] as VALID number pairs!
                l, r = 0, M - 1
                while l <= r:
                    mid = (l + r) // 2
                    num2 = nums2[mid]
                    if num2 >= threshold:
                        # Valid solution, look for even more valid leftmost ones
                        r = mid - 1
                    else:
                        # Invalid solution, look for valid ones on right
                        l = mid + 1
                
                # Every product between num1 and any number in nums2[leftmost..M-1]
                # is valid. Hence, there are M - leftmost total valid products
                res += M - l

            return res
        
        edge_cases = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        ]
        min_product = min(edge_cases)
        max_product = max(edge_cases)
        if k == 1:
            return min_product
        if k == N * M:
            return max_product

        # Find leftmost product where it is the case that count == k
        l, r = min_product, max_product
        leftmost = None
        while l <= r:
            mid = (l + r) // 2
            count = getProductCount(mid)
            if count >= k:
                # k'th smallest product is SMALLER, so search on left
                leftmost = mid
                r = mid - 1
            else:
                # k'th smallest product is LARGER, so earch on right
                l = mid + 1

        return leftmost
