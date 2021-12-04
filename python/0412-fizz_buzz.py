
# 412. Fizz Buzz

# https://leetcode.com/problems/fizz-buzz/
# https://medium.com/@Bear_/%E7%B0%A1%E5%96%AE%E7%9A%84-fizzbuzz-%E8%97%8F%E6%9C%89-%E6%B7%B1%E5%BA%A6-google-%E9%9D%A2%E8%A9%A6%E9%A1%8C-f5e66e3a97be
# https://joelgrus.com/2016/05/23/fizz-buzz-in-tensorflow/


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            text = ''
            if i % 3 == 0:
                text += 'Fizz'
            if i % 5 == 0:
                text += 'Buzz'
            if len(text) == 0:
                text += str(i)
            result.append(text)
        return result
