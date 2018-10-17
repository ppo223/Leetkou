class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # if len(nums) * len(nums[0]) != r * c:
            # return nums
        # else:
            # nums_list = []
            # rows,rols = len(nums),len(nums[0])
            # for i in range(rows):
                # for j in range(len(nums[i])):
                    # nums_list.append(j)
            
            # new_nums = []
            # for ni in range(r):
                # new_nums.append([])
                # for nj in range(c):
                    # new_nums[i].append(nums[i])
                    # pass
            # return nums_list
        temp = []
        res = []
        for i in nums :
            temp.extend(i)
        if len(temp) == r*c :
            for i in range(r) :
                x = []
                for j in range(c) :
                    x.append(temp[i*c+j])
                res.append(x)
        else :
            return nums 
        return res 
                    
                    
        
