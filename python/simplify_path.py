
# 71. Simplify Path

# https://leetcode.com/problems/simplify-path/
# https://leetcode.com/problems/simplify-path/discuss/25691/9-lines-of-Python-code


class Solution(object):
    def simplifyPath(self, path: str) -> str:
        # My method
        path = re.sub(r'/+', '/', path)
        stack = []
        for element in path.split('/'):
            if not element:
                continue
            if element == '.':
                continue
            elif element == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(element)
        return '/' + '/'.join(stack)


        # Concise version
        # elements = [e for e in path.split('/') if e != '.' and e != '']
        # stack = []
        # for element in elements:
        #     if element == '..':
        #         if len(stack) > 0:
        #             stack.pop()
        #     else:
        #         stack.append(element)
        # return '/' + '/'.join(stack)
