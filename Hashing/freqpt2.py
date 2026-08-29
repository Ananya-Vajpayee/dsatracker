from collections import defaultdict
class Solution:
    def Frequency(self, arr, n):
        freq_map=defaultdict(int)
         # Traverse the array and count frequencies
        for i in range(n):
           freq_map[arr[i]]+=1
         # Traverse through the defaultdict and print frequencies
        for key, value in freq_map.items():
           print(f"Element: {key}, Frequency: {value}")
if __name__ == "__main__":
    # Input array
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)

    # Create Solution instance
    sol = Solution()

    # Call the function to count frequencies
    sol.Frequency(arr, n)
