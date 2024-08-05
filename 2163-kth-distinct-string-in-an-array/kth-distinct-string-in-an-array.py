class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = set()
        seen = set()

        for string in arr:
            if string not in seen:
                # First time we see string
                distinct.add(string)
            elif string in distinct:
                # 2nd time we see string
                distinct.remove(string)
            seen.add(string)
        
        if len(distinct) < k:
            return ""

        seen.clear()
        for string in arr:
            if string in distinct:
                seen.add(string)
                if len(seen) == k:
                    return string
        
        raise Exception("Unreachable code")
