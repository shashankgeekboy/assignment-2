def longest_harmonious_subsequence(nums):

  max_value = nums[0]
  min_value = nums[0]
  max_length = 1
  for num in nums:
    if num > max_value:
      max_value = num
      max_length = 1
    elif num < min_value:
      min_value = num
      max_length = 1
    else:
      max_length += 1
  return max_length
nums = [1, 3, 2, 2, 5, 2, 3, 7]

longest_harmonious_subsequence(nums)
