class Solution:
    
    def majorityElementRec(self, nums, left, right):
        if left == right:
            return nums[left]
        
        mid = left + (right - left) // 2
        
        left_majority = self.majorityElementRec(nums, left, mid)
        right_majority = self.majorityElementRec(nums, mid + 1, right)
        
        if left_majority == right_majority:
            return left_majority
        
        left_count = self.countInRange(nums, left_majority, left, right)
        right_count = self.countInRange(nums, right_majority, left, right)
        
        return left_majority if left_count > right_count else right_majority
    
    def countInRange(self, nums, val, left, right):
        count = 0
        for i in range(left, right + 1):
            if nums[i] == val:
                count += 1
        return count
    
    def majorityElement(self, nums):
        return self.majorityElementRec(nums, 0, len(nums) - 1)
