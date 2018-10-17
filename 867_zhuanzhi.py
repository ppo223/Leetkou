a = [[1,2],[3,4],[5,6]]

rows = len(a)
rols = len(a[0])
res = []

for i in range(rols):
    res.append([])
    for j in range(rows):
        res[i].append(a[j][i])
print(res)



#leetcode
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        a = [[] for i in A[0]]
        for i in A:
            for j in range(len(i)):
                a[j].append(i[j])
        return a
    
