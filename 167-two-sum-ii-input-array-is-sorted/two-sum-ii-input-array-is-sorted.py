class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        step_left = 1
        step_right = len(numbers)
        left_pointer = 0
        right_pointer = -1
        for i in range(step_right):
            if(numbers[left_pointer] + numbers[right_pointer] > target):
                right_pointer -= 1
                step_right -= 1
            elif(numbers[left_pointer] + numbers[right_pointer] < target):
                left_pointer += 1
                step_left += 1
            else:
                break
        
        return [step_left, step_right]