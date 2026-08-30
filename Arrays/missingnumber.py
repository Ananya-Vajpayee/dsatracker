def missingnumber(arr):
    n=len(arr)+1
    total_sum=sum(arr)
    expected_sum=n*(n+1)//2
    return expected_sum-total_sum
if __name__=="__main__":
    arr=[1,2,3,5]
    print("missing number:", missingnumber(arr))