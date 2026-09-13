class Solution():
    def linearsearch(self,nums,num):
        n=len(nums)
        for i in range(n):
            if nums[i]==num:
                return True
        return False
    def longestsequence(self,nums):
        n=len(nums)
        if n==0:
            return 0
        longest=1
        for i in range(n):
            x=nums[i]
            cnt=1
            while self.linearsearch(nums,x+1):
                cnt+=1
                x+=1
            longest=max(longest,cnt)
        return longest
