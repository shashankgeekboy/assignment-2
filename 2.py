def max_different_candies(candyType):

  candy_counts = {}
  for candy in candyType:
    if candy not in candy_counts:
      candy_counts[candy] = 0
    candy_counts[candy] += 1

  max_different_candies = 0
  for candy, count in candy_counts.items():
    if count > max_different_candies:
      max_different_candies = count

  return max_different_candies
candyType = [1, 1, 2, 2, 3, 3]

max_different_candies(candyType)
print(candyType)
