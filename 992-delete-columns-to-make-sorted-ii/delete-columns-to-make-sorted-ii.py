class Solution:
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        res = 0
        sorted_pairs = [False] * (n - 1)

        for col in range(m):
            bad = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                res += 1
                continue

            for i in range(n - 1):
                if strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True

        return res

# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         # There's gotta be some index i where strs is lexicographically sorted given
#         # strs[0][i], strs[1][i], ..., str[N-1][i]. Let's find first such index
#         N = len(strs)
#         L = len(strs[0]) # all strings have same length L
#         indices = []
#         weak_indices = [] # in case of ties

#         # index = None
#         for i in range(L):
#             letters = [s[i] for s in strs]
#             prev = letters[0]
#             is_ordered = True
#             is_weak = False
#             for j in range(1, N):
#                 if prev > (letter := letters[j]):
#                     is_ordered = False
#                     break
#                 elif prev == letter:
#                     is_weak = True
#                 prev = letter

#             # We must delete every index beforehand, of which there are 'i' many
#             if is_ordered:
#                 # index = i
#                 # break
#                 if is_weak:
#                     weak_indices.append(i)
#                 else:
#                     indices.append(i)

#         # Must delete all indices
#         if len(weak_indices) == len(indices) == 0:
#             return L
        
#         if len(weak_indices) == 0:
#             return indices[0] # Delete all up to this index
        
#         if len(indices) == 0:
#             # return L - len(weak_indices)
#             deleted_indices = set()
#             for i in range(weak_indices[0]):
#                 deleted_indices.add(i)
            
#             j = weak_indices[0] + 1
#             del_strs = []
#             # for s in strs:
#             #     s = "".join(s[i] for i in range(L) if i not in deleted_indices)
#             #     del_strs.append(s)
#             # print(f"{del_strs=}")
#             while (del_strs := ["".join(s[i] for i in range(L) if i not in deleted_indices) for s in strs]) != sorted(del_strs):
#                 print(f"{del_strs=}, {sorted(del_strs)=}, {deleted_indices=}")
#                 assert j < L
#                 deleted_indices.add(j)
#                 j += 1
            
#             # res = weak_indices[0] # delete everything up to first
#             return len(deleted_indices)

#         assert len(indices) > 0 and len(weak_indices) > 0
#         if indices[0] < weak_indices[0]:
#             return indices[0]
    
#         # Here, we have weak_indices[0] < indices[0]. We obviously
#         # only care about weak_indices smaller than indices[0], and
#         # in fact the solution is to delete all indices prior to
#         # indices[0] that are not a weak_index
#         # res = indices[0]
#         # for index in weak_indices:
#         #     if index < indices[0]:
#         #         res -= 1
#         #     else:
#         #         break
#         # print(f"{indices=}")
#         # print(f"{weak_indices=}")
#         # return res 
        
#         # At any point, we can pick indices[0] as our solution.
#         # Or, we can delete everything up to weak_indices[0],
#         # and then choose again
#         # N, M = len(indices), len(weak_indices)
#         # self.indices, self.weak_indices = indices, weak_indices

#         # Step 1: Everything up to weak_indices[0] must be deleted
#         res = weak_indices[0]
#         weak_indices_set = set(weak_indices)

#         # Step 2: Check if we must delete each index up to indices[0]
#         strings = [[s[weak_indices[0]]] for s in strs] # keep as inner-lists for easy append / pop
#         def add_letter(index):
#             for i, l in enumerate(strings):
#                 l.append(strs[i][index])
#         def pop_letter():
#             for l in strings:
#                 l.pop()
#         for index in range(weak_indices[0] + 1, indices[0]):
#             if index in weak_indices_set:
#                 add_letter(index)
#                 continue
            
#             add_letter(index)
#             if not self.is_lexicographically_sorted(strings):
#                 pop_letter()
#                 res += 1
        
#         return res


    
#     def is_lexicographically_sorted(self, arr):
#         if len(arr) == 0:
#             return True
        
#         prev = arr[0]
#         for i in range(1, len(arr)):
#             if prev > (cur := arr[i]):
#                 return False

#             prev = cur

#         return True


#     @cache
#     def dp(self, i, j):
#         indices, weak_indices = self.indices, self.weak_indices
#         N, M = len(indices), len(weak_indices)





#         # print(f"{indices=}")
#         # print(f"{weak_indices=}")
#         # return -1
#         # if index is None:
#         #     return L
        
#         # # Now, the strings may still not be lexicographically sorted in cases such as
#         # # 'xga' and 'xfb' where xga should go AFTER xfb, despite their first letter (x) being
#         # # lexicographically sorted already. 
        