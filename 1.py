def max_pair_sum(nums):
  nums.sort()
  sum = 0
  for i in range(len(nums) // 2):
    sum += min(nums[2 * i], nums[2 * i + 1])
  return sum
nums = [1, 4, 2, 3, 5, 6]

max_pair_sum(nums)
print(nums)
