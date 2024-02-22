class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token != '+' and token != '*' and token != '-'and token != '/':
                stack.append(token)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(int(num1) + int(num2))
                elif token == '-':
                    stack.append(int(num2) - int(num1))
                elif token == '*':
                    stack.append(int(num1) * int(num2))
                else:
                    stack.append(int(num2) /int(num1))
        val = stack.pop()
        return int(val)        