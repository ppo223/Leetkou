

nums = []
nums.sort()
a = 0
for i in range(0,len(nums),2):
    a += min(nums[i],nums[i+1])
#    return a
    print(a)       



class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = 0
        for i in range(0,len(nums),2):
            a += min(nums[i],nums[i+1])
        return a
        
         
