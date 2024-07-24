class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left


result = Solution()
nums = [1, 3, 5, 6]
target = 7
nums = [1, 3, 5, 6]
target = 5
print(result.searchInsert(nums, target))



