class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operators = ["+", "-", "*", "/"]

        for x in tokens:
            if x in operators:
                b = numStack.pop()
                a = numStack.pop()
                if x == "+":
                    numStack.append(a + b)
                elif x == "-":
                    numStack.append(a - b)
                elif x == "*":
                    numStack.append(a * b)
                else:
                    numStack.append(int(a / b))
            else:
                numStack.append(int(x))

        return numStack[0]