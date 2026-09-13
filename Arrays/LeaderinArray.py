class Solution:
    def leaderinarray(self,nums):
        n=len(nums)
        ans=[]
        if not nums:
            return ans
        max_val=nums[-1]
        ans.append(nums[n-1])
        for i in range(n-2,-1,-1):
            if nums[i]>max_val:
                ans.append(nums[i])
                max_val=nums[i]
        ans.reverse()
    
        return ans
nums = [10, 22, 12, 3, 0, 6]
finder=Solution()
answer=finder.leaderinarray(nums)
print("Leaders in the array are:", answer)

