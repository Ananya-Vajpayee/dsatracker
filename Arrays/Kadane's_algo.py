#max sum in subarray
from typing import List

class Solution:
    # Function to find maximum sum of subarrays
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxi=nums[0]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>maxi:
                maxi=sum
            if sum<0:
                sum=0
        return maxi
if __name__ == "__main__":
    arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]

    # Create an instance of Solution class
    sol = Solution()

    maxSum = sol.maxSubArray(arr)

    # Print the max subarray sum
    print(f"The maximum subarray sum is: {maxSum}")