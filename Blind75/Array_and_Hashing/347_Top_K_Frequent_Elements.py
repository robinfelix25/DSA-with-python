


#Solution : 1
"""
This solution 
- first counts the frequency
- Then sorted the dictionary
- then take the last k occurances
I think the runtime complexity will be O(n log n) + o(k), Since Python sorted() is nlogn, so O(n) + O(n log(n)) + O(k)
There an another way using MaxHeap need to look into that
"""
def topKFrequentSorted(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hashmap = {}

    for n in nums:
        hashmap[n] = 1 + hashmap.get(n, 0)
    
    # print(hashmap)
    sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1])
    # print (sorted_hashmap)
    # print (sorted_hashmap[-2][1])
    result = []
    for i in range(1,k+1):
            result.append(sorted_hashmap[-1 * i][0])
    return result

nums = [1,1,1,2,2,3]
k = 2
# print(topKFrequentSorted(nums, k))


def topKFrequent(nums, k):
    count = {}
    buckets = len(nums) + 1
    # freq1 = [[]] * buckets
    freq = [[] for _ in range(len(nums)+1)]

    for i in nums:
        count[i] = 1 + count.get(i, 0)
    print(count)

    for k,v in count.items():
         print(k,v)
         freq[v].append(k)
    print(freq)

    res = []
    for i in range(len(freq)-1, 0, -1):
         if len(i) != 0:
              res.append(freq[i][0])
         if len(res) == k:
              break
    return res

topKFrequent
         

topKFrequent(nums, k)   