#Bruteforce
class ArrayManipulator:
    def elements_by_sign(self,arr,n):
        pos_arr=[]
        neg_arr=[]
        for i in range(n):
            if arr[i]>=0:
                pos_arr.append(arr[i])
            else:
                neg_arr.append(arr[i])
        for i in range(n//2):
            arr[2*i]=pos_arr[i]
            arr[2*i+1]=neg_arr[i]
        return arr
if __name__=="__main__":
    arr=[1,2,3,-4,-1,-6]
    n=len(arr)
    obj=ArrayManipulator()
    sol=obj.elements_by_sign(arr,n)
    print("The array after rearranging elements by sign is:",sol)

    #Complexity Analysis:
    # Time Complexity: O(n+n/2), where n is the number of elements in the input array

    #Optimal Solution
class ArrayManipulator:
    def elements_by_sign(self,A):
        n=len(A)
        ans = [0] * n  # Initialize result array with zeros
        pos_index=0
        neg_index=1
        for i in range(n):
            if A[i]>=0:
                ans[pos_index]=A[i]
                pos_index+=2
            else:
                ans[neg_index]=A[i]
                neg_index+=2
        return ans
if __name__=="__main__":
    arr=[0,1,5,6,-2,-3,-4]
    obj=ArrayManipulator()
    sol=obj.elements_by_sign(arr)
    print("The array after rearranging elements by sign is:",sol)

    #Complexity Analysis:
    # Time Complexity: O(n), where n is the number of elements in the input array