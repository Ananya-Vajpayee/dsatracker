# Class to solve 3-sum problem
class Solution:
    # Function to find triplets with sum zero
    def threeSum(self, arr, n):
        ans=set()
        for i in range(n):
            hashnet=set()
            for j in range(i+1,n):
                third=-(arr[i]+arr[j])
                if third in hashnet:
                    triplet=tuple(sorted((arr[i],arr[j],third)))
                    ans.add(triplet)
                # Add current element to set
                hashnet.add(arr[j])

        # Convert set to list of lists
        return [list(triplet) for triplet in ans]
            