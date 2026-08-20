class Solution:
    def findmaxconsecutiveones(self, nums):
        count=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count=0
            maxi=max(maxi, count)
        return maxi
nums = [1, 1, 0, 1, 1, 1]


obj = Solution()

# Get answer
ans = obj.findmaxconsecutiveones(nums)

# Print result
print("The maximum consecutive 1's are", ans)