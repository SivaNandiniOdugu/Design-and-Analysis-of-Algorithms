
# Print all permutation using backtracking
def backtrack(selected, count):
    global nums, n
    if count == n: 
       print(selected) # all permutation
    
    # Explore next elements
    for i in range(n):
      if nums[i] not in selected:
        selected.append(nums[i])
        backtrack(selected, count + 1)  # move to next index
        selected.pop()  # backtrack

# Example
nums = [1, 2, 3]
n = len(nums)
backtrack([], 0)


