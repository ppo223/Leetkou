class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # a_d = dict((nums.count(x),x) for x in nums)    ##############
        # max_ = max(a_d.keys())    ############
        # k = [k for k,v in a_d.items() if v == max_]
        # for i in k:
            # return i
        # for i in a_d.keys():
        #     if a_d.get(i) == max_:
        #         return i
        # return a_d[max_]            ########
        
        # for key in a_d:
            # if a_d[key] == max_:
                # return key
                
                
        nums.sort()
        # b = len(nums) // 2
        # return nums[b]
    
        return nums[len(nums)//2]
        
