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
            
            if is_subfolder == False:
                res.append(folder)
        
        return res