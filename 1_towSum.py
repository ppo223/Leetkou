
nums = [3,3,2,4,5]
target = 6


def twoSum(nums,target):
    a = {}
    for i in range(len(nums)):
        b = target - nums[i]
        if b in a:
            return [a[b],i]
        a[nums[i]] = i


print(twoSum(nums,target))


#leetcode
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in a:
                return [a[b],i]
            a[nums[i]] = i
     
            
