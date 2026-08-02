class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        zeros = 0

        total_product = 1
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total_product *= num
        
        if zeros > 1:
            return [0] * len(nums)
        
        for num in nums:
            if zeros == 1:
                if num:
                    output.append(0)
                else:
                    output.append(total_product)
            else:
                output.append(total_product // num)
        
        return output
        