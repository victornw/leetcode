class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = -1
        lenght = len(numbers)
        for i in range(lenght):
            if(numbers[left_pointer] + numbers[right_pointer] > target):
                right_pointer -= 1
            elif(numbers[left_pointer] + numbers[right_pointer] < target):
                left_pointer += 1
            else:
                break
        
        return [left_pointer + 1, (lenght + right_pointer) + 1]