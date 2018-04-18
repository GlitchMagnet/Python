nums = [1,4,2,4]
maxes = [3,5]
m = len(maxes)
n = len(nums)

def binary_search(array, n, max_target): #binary search type so no need to recurse
    low = 0
    high = n-1
    while(low <= high):                 
        middle = int((low + high)//2)       #find middle index
        if(array[middle] <= max_target):    #compare element at middle to find largest element in nums <= target element in maxes
            low = middle + 1
        else:
            high = middle - 1
    return high

def counts(nums, maxes):
    answer = []                         #create list to hold final answer
    nums.sort()                         #sort to achieve O(nlogn) time complexity
    for i in range(m): 
        target_index = binary_search(nums, n, maxes[i])         #have to write some sort of binary search algorithm
        count = target_index + 1                                #when target index found, all elements smaller than this index will be correct,
                                                                #add 1 to account for this element
        answer.append(count)                                    #add count to our list of answers
    return answer

if __name__ == "__main__":
    result = counts(nums, maxes)
    print(result)
