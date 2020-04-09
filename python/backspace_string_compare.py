
# 844. Backspace String Compare

# https://leetcode.com/problems/backspace-string-compare/
# https://leetcode.com/problems/backspace-string-compare/discuss/145786/Python-tm


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_char(string, pointer):
            char, count = '', 0
            while pointer >= 0 and not char:
                if string[pointer] == '#':
                    count += 1
                elif count == 0:
                    char = string[pointer]
                else:
                    count -= 1
                pointer -= 1
            return char, pointer
        
        # Two pointer with Space Complexity O(1)
        pointer_s, pointer_t = len(S) - 1, len(T) - 1
        while pointer_s >= 0 or pointer_t >= 0:
            s = t = ''
            if pointer_s >= 0:
                s, pointer_s = get_char(S, pointer_s)
            if pointer_t >= 0:
                t, pointer_t = get_char(T, pointer_t)
            if s != t:
                return False
        return True


        # Another method
        # Solve by using stack with Space Complexity O(N)
        stack_s, stack_t = [], []
        for s in S:
            if s.isalpha():
                stack_s.append(s)
            elif s == '#' and stack_s:
                stack_s.pop()
        for t in T:
            if t.isalpha():
                stack_t.append(t)
            elif t == '#' and stack_t:
                stack_t.pop()

        while stack_s and stack_t:
            s = stack_s.pop()
            t = stack_t.pop()
            if s != t:
                return False
        return True if not stack_s and not stack_t else False
