"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4  # ไม่แน่ใจว่าเป็็น index ที่ 5 หรือป่าวครับ ?

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        max_index = 0
        if not numbers:
            return "list can not be blank"
        max_value = numbers[0]
        for index in range (len(numbers)):
            # print(numbers[index])
            if numbers[index] > max_value:
                max_value = numbers[index]
                max_index = index
        return max_index

result = Solution()
print(result.find_max_index([1, 2, 1, 3, 5, 6, 4]))  
print(result.find_max_index([]))          
        
