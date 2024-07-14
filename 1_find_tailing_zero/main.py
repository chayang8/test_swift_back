"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    
    def find_tailing_zeroes(self, number: int) -> int | str:
        zero = 0
        factor = 5
        if number < 0:
            return "number can not be negative"
        while number // factor >= 1:
            zero += number // factor
            print(number // factor)
            factor *= 5
        return zero

result = Solution()
print(result.find_tailing_zeroes(4))  
print(result.find_tailing_zeroes(-10))  
