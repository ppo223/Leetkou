class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in nums:
        #     if i == 0:
        #         nums.remove(i)
        #         nums.append(i)
        # return nums
        
        
        # for i in nums[-1::-1]:
            # if i == 0:
                # del nums[i]
                # nums.append(0)
        # return nums
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
        nums.extend([0]*count)
        
