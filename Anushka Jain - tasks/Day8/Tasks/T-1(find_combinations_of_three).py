def find_combinations_of_three(nums, target):
    nums = list(set(nums))
    result = set()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            complement = target - nums[i] - nums[j]

            #Check if complement exists in the remaining part of nums
            if complement in nums[:i] + nums[j+1:]:
                result.add(tuple(sorted((nums[i], nums[j], complement))))
    return list(result);

    
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_val = 12
print(find_combinations_of_three(nums,target_val))


