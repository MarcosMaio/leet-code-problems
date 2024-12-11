from typing import List
nums = [2,-1,1]

# se possuir dois números iguais, retornar o número positivo

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
      nums.sort(key=lambda x: (abs(x), -x))
      min_abs_num = min(nums, key=abs)
      return min_abs_num
      

result = Solution.findClosestNumber(Solution,nums)
print(result)