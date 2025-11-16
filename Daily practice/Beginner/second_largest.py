def second_largest(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None


numbers = [4, 1, 7, 3, 9]
print(second_largest(numbers))
