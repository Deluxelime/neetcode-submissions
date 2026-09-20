class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     index = nums[i]
        #     for j in range(i+1, len(nums)):
        #         index2 = nums[j]
        #         if index2 == index:
        #             return True
        # return False
        list.sort(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
            