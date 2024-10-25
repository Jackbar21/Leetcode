class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders = set(folder)
        res = []

        for folder in folders:
            is_subfolder = False
            for i in range(1, len(folder)):
                if folder[i] == "/" and folder[:i] in folders:
                    is_subfolder = True
                    break
            
            # Valid folder if and only if it's NOT a subfolder.
            if not is_subfolder:
                res.append(folder)
        
        return res