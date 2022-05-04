from pythonds import Stack


def inToPre(infixexp):
    infixList = infixexp.split()
    infixList.reverse()
    output = []
    stack = Stack()
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, ")": 1}
    for token in infixList:
        if token not in "()*/+-^":
            output.append(token)

        elif token == ")":
            stack.push(token)

        elif token == "(":
            top = stack.pop()
            while top != ")":
                output.append(top)
                top = stack.pop()

        elif token == "^":
            while not stack.isEmpty() and prec[token] <= prec[stack.peek()]:
                output.append(stack.pop())
            stack.push(token)

        else:
            while not stack.isEmpty() and prec[token] < prec[stack.peek()]:
                output.append(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        output.append(stack.pop())

    output.reverse()
    return " ".join(output)

#########################################   EValuator     #################################################

def prefixEval(prefixExpr):
    operandStack = Stack()
    tokenList = prefixExpr.split()
    tokenList.reverse()

    for token in tokenList:
        if token not in "+-*/^":
            operandStack.push(float(token))

        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
            
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "^":
        return op1 ** op2
    else:
        return op1 - op2


infix = input("Enter an infix expression: \n'separate between each element with space'\n")
prefix = inToPre(infix)
print("equivalent prefix: \n", prefix)
print("Result of evaluation: \n", prefixEval(prefix))