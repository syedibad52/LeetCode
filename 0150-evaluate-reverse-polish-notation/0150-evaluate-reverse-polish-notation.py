class Solution:
    def evalRPN(self, tokens):
        stack = []

        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append((abs(a) // abs(b)) * (1 if a * b >= 0 else -1))
            else:
                stack.append(int(t))

        return stack.pop()