def max_product_of_three(nums):
  max1 = max2 = max3 = -float("inf")
  for num in nums:
    if num > max1:
      max3 = max2
      max2 = max1
      max1 = num
    elif num > max2:
      max3 = max2
      max2 = num
    elif num > max3:
      max3 = num
  return max(max1 * max2 * max3, max1 * max2, max1 * max3)


if __name__ == "__main__":
  nums = [1, 2, 3]
  print(max_product_of_three(nums))
