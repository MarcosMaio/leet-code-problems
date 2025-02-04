# 1800. Maximum Ascending Subarray Sum

# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.

# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

# Example 1:

# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
# Example 2:

# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
# Example 3:

# Input: nums = [12,17,15,13,10,11,12]
# Output: 33
# Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.


from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                
                if current_sum > max_sum:
                    max_sum = current_sum

                
                current_sum = nums[i]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum

nums = [12, 17, 15, 13, 10, 11, 12]
solution = Solution()
resultado = solution.maxAscendingSum(nums)
print(f"Resultado: {resultado}")


# nums = [9,1,3,4]

# class Solution:
#     def maxAscendingSum(self, nums: List[int]) -> int:
      
#       if len(nums) == 1:
#         return nums[0]
      
#       acending_subarray_sum: list[int] = []
#       temp = int(0)
      
#       for i in range(len(nums) - 1):
#         if nums[i] < nums[i + 1]:
#           if temp == 0:
#             temp = nums[i] + nums[i + 1]
#           else:
#             temp = temp + nums[i + 1]
#         else:
#           if temp != 0:
#             acending_subarray_sum.append(temp)
#             temp = 0
            
#       if temp != 0:
#           acending_subarray_sum.append(temp)
          
#       return max(acending_subarray_sum) if acending_subarray_sum else max(nums)
    

# solution = Solution()
# result = solution.maxAscendingSum(nums)
# print(result)



