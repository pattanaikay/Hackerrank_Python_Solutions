# two-sum

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

'''
class Solution:
    def two_sum(self, nums, target):
        
        num_dict = {}

        for i, num in enumerate(nums):

            temp = target - num

            if temp in num_dict:
                return (num_dict[temp], i)
            
            else:
                num_dict[num] = i
        
        return []
    
sol_class = Solution()
nums = [2, 7, 11, 15]
target = 9
result = sol_class.two_sum(nums, target)
print(result)

