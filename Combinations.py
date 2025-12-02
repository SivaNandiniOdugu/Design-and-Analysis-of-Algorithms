# Print all combination using backtracking
def backtrack(selected, cur_Ind):
    global nums, n
    #print(selected) # all combination
    if cur_Ind == n: 
       print(selected) # all combinatinetorial solution
    
    # Explore next elements
    for i in range(cur_Ind, n):
        selected.append(nums[i])
        backtrack(selected, i + 1)  # move to next index
        selected.pop()  # backtrack

# Example
nums = [1, 2, 3]
n = len(nums)
backtrack([], 0)