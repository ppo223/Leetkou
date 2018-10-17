# -*- coding:utf-8 -*-
#一行代码搞定：将数字转换成字符列表，切片方法搞定
#return True if str(x) == str(x)[::-1] else False



class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # for i in x_list[-1::-1]:
            # for j in x_list[-1::-1]:
                # if i == j :
                    # return (i == j)
                # else:
                    # return (i == j)
        # if x >=0 :
            # x_str = str(x)
            # if x_str == x_str[::-1]:
                # return (1 == 1)
            # else:
                # return (1 == 0)
        # else:
            # return (1==0)
        return True if str(x) == str(x)[::-1] else False


