nums = [4, 5, 12, 45, 98, 1, 2]

print('Then', nums)

for i in range(len(nums)):
    lowest = i

    for j in range(i+1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j

    nums[i], nums[lowest] = nums[lowest], nums[i]

print('Now', nums)
