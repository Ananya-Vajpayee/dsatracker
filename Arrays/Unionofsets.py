class Solution:
    def union(self,arr1,arr2):
        st=set(arr1) | set(arr2)
        return sorted(st)
arr1=[1,2,3,4,5]
arr2=[7,8,9,10]
obj=Solution()
result=obj.union(arr1,arr2)
print("Union of two arrays is:", result)