"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0 or number > 10000000:
            return "number can not less than 0 or more than 10,000,000"

        if number == 0:
            return "ศูนย์"
        thai_digits = [
            "", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า",
            "หก", "เจ็ด", "แปด", "เก้า", "สิบ"
        ]
        thai_place_values = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        number_str = str(number)
        length = len(number_str)
        thai_text = []
        for i, digit_char in enumerate(number_str):
            digit = int(digit_char)
            place_value = length - i - 1 
            if digit == 2 and place_value == 1:
                thai_text.append("ยี่สิบ")
            elif digit == 1 and place_value == 1:
                thai_text.append("สิบ")
            elif place_value == 0:
                thai_text.append("เอ็ด")
            else:
                thai_text.append(thai_digits[digit] + thai_place_values[place_value])

        return "".join(thai_text)
result = Solution()
print(result.number_to_thai(101))  
print(result.number_to_thai(1222))  
print(result.number_to_thai(-1))