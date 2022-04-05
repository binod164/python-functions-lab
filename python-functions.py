#1 Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  sum = 0
  for num in range(1, n+1):
    sum += num
  return sum

#2 Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  largest_num = 0
  for num in nums:
    if num > largest_num:
      largest_num = num
  return largest_num

#3 Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurances(string, substr):
  return string.count(substr)

#4 Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  result = 1
  for arg in args:
    result *= arg
  return result
