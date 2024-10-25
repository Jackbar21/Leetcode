class Solution:
    def isSubfolder(self, subfolder, folder):
        # Check if folder is a PREFIX of subfolder
        return folder[:len(subfolder)] == subfolder # TODO: Optimize this
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 4 * 10^4 * 100 == 4 * 10^4 * 10^2 == 4 * 10^6
        folders = set(folder)
        res = []

        for folder in folders:
            slash_indices = []
            for index in range(1, len(folder)):
                if folder[index] == "/":
                    slash_indices.append(index)

            is_subfolder = False
            for slash_index in slash_indices:
                if folder[:slash_index] in folders:
                    is_subfolder = True
                    break
            
            if is_subfolder == False:
                res.append(folder)
        
        return res