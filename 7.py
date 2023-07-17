def is_monotonic(nums):
  increasing = True
  decreasing = True
  for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
      increasing = False
    elif nums[i] > nums[i - 1]:
      decreasing = False
  return increasing or decreasing


if __name__ == "__main__":
  nums = [1, 2, 2, 3]
  print(is_monotonic(nums))
