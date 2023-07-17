def min_score(nums, k):
  min_val = nums[0]
  max_val = nums[0]
  for i in range(1, len(nums)):
    min_val = min(min_val, nums[i] - k)
    max_val = max(max_val, nums[i] + k)
  return max_val - min_val


if __name__ == "__main__":
  nums = [1]
  k = 0
  print(min_score(nums, k))
