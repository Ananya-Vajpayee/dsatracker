n=int(input()) # how many numbers are in the array
arr=list(map(int, input().split())) # read the array itself
#hash_ = Counter(arr)          # builds {value: count} automatically If values aren't guaranteed to be small (0–12)
hash_map=[0]*13  # a "bucket" for each possible value 0–12, all start at 0
for x in arr:
    hash_map[x]+=1 # for every number we see, increment its bucket
q=int(input()) # how many queries
for _ in range(q):
    query=int(input()) # read the query number(value being asked about)
    print(hash_map[query]) # print how many times it appeared in the array