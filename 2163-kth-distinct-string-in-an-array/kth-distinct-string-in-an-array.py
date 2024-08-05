class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = set()
        seen = set()

        for string in arr:
            if string not in seen:
                # First time we see string
                distinct.add(string)
            else:
                # 2nd or more time we see string
                if string in distinct:
                    distinct.remove(string)
            seen.add(string)
        
        # print(distinct, seen)
        seen.clear()

        for string in arr:
            if string in distinct:
                seen.add(string)
                if len(seen) == k:
                    return string
        
        return ""
