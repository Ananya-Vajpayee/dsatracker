#brute force
class Solution:
    # Function to calculate max profit using brute force
    def stockbuySell(self, prices):
        # Initialize max profit to 0
        maxProfit = 0

        # Loop through each day as potential buy day
        for i in range(len(prices)):
            # Loop through future days as potential sell day
            for j in range(i + 1, len(prices)):
                # Calculate profit
                profit = prices[j] - prices[i]

                # Update max profit if higher
                maxProfit = max(maxProfit, profit)

        # Return the maximum profit
        return maxProfit

# Driver code
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print("Max Profit:", sol.stockbuySell(prices))

#Optimal solution
class Solution:
    # Function to calculate maximum profit using single pass
    def stockbuySell(self, prices):
        # Initialize the minimum price to a large number
        min_price = float('inf')

        # Initialize the maximum profit to 0
        max_profit = 0

        # Traverse each price in the array
        for price in prices:
            # If current price is less than min_price, update min_price
            if price < min_price:
                min_price = price
            # Else calculate profit and update max_profit if it's greater
            else:
                max_profit = max(max_profit, price - min_price)

        # Return the maximum profit found
        return max_profit

# Driver code
obj = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(obj.stockbuySell(prices))