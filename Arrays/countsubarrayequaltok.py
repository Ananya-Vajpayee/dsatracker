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

#better approach
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        prefix_counts = {0: 1}  # empty prefix sum occurs once

        for num in nums:
            running_sum += num
            count += prefix_counts.get(running_sum - k, 0)
            prefix_counts[running_sum] = prefix_counts.get(running_sum, 0) + 1

        return count