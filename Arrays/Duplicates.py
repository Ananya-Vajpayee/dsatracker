class Solution:
    def removeduplicates(self,num):
        if not nums:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1
nums=[0,0,1,1,2,3,4,4,5,5,5]
sol=Solution()
k=sol.removeduplicates(nums)
print("Unique count ",k)
print("Array after removing duplicates:", nums[:k])
    
        