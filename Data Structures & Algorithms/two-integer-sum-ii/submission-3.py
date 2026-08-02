class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            complement = target - numbers[i]
            l = i + 1
            r = len(numbers) - 1

            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    l = mid + 1
                else:
                    r = mid - 1
