from typing import List

strs = ["flower", "flow", "flight"]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result


result = Solution.longestCommonPrefix(Solution, strs)

print(result)
