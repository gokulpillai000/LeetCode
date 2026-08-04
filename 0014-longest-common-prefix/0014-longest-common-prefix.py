class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        prefix = ''
        for i in range(len(first)):
            ch = first[i]
            for j in range(1, len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=ch: #if strs[j] is lessthan the length of first then the prefix is not may occur
                    return prefix
                    exit()
            prefix+=ch
        return prefix
        