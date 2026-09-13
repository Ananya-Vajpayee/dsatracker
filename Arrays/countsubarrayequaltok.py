class Solution:
    def subarraySum(self, nums, k):
        count=0
        n=len(nums)
        for i in range(n):
            total=0
            for j in range(i,n):
                total+=nums[j]
                if total==k:
                    count+=1
        return count
arr = [3, 1, 2, 4]
k=6
finder=Solution()
print(finder.subarraySum(arr,k))
