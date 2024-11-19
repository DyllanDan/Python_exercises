def sort_list(nums):
    a = True
    while a:
        i = 0
        for num in nums:
            if i < (len(nums) - 1) and num > nums[i + 1]:
                b = num
                nums[i] = nums[i + 1]
                nums[i + 1] = b
            i += 1
        i = 0
        while i < (len(nums) - 1):
            if nums[i] > nums[i + 1]:
                a = True
                break
            else:
                a = False
            i += 1
    return nums


random_num = [60, 1, 30, 5, 2, 10, 45, 20, 46, 12, 14]
print(random_num)
print(sort_list(random_num))
