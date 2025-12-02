def sum_of_subsets(nums, target):
    res = []
    def backtrack(i, path, total):
        if total == target:
            res.append(path)
            return
        if i >= len(nums) or total > target:
            return
        backtrack(i + 1, path + [nums[i]], total + nums[i])
        backtrack(i + 1, path, total)
    backtrack(0, [], 0)
    return res

nums = [10, 7, 5, 18, 12, 20, 15]
target = 35
print("Sum of Subsets:", sum_of_subsets(nums, target))