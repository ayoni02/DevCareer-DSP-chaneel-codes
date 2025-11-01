def is_sorted(nums):
    if nums == sorted(nums):
        return "yes, ascending"
    elif nums == sorted(nums, reverse=True):
        return "yes, descending"
    else:
        return "no"