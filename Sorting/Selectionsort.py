class Solution:
    def SelectionSort(self,arr):
        n=len(arr)
        for i in range(n-1):
            min_index=i
            for j in range(i+1,n):
                if arr[j]<arr[min_index]:
                  min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        print("Sorted array is:",arr)
        print("Time complexity of selection sort is O(n^2)")

arr = [13, 46, 24, 52, 20, 9]

# Print array before sorting
print("Before selection sort:")
print(*arr)

# Call selection sort
sol = Solution()
sol.SelectionSort(arr)
