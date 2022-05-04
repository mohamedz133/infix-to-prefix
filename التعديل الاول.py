from pythonds import Stack


def inToPre(infixexp):
    infixList = infixexp.split()
    output = []
    stack = Stack()
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, ")": 1}

    for token in infixList[::-1]:

        if token not in "()*/+-^":
            output.insert(0, token)
        elif token == ")":
            stack.push(token)

        elif token == "(":
            top = stack.pop()
            while top != ")":
                output.insert(0, token)
                top = stack.pop()

        elif token == "^":
            while not stack.isEmpty() and prec[token] <= prec[stack.peek()]:
                output.insert(0, stack.pop())
            stack.push(token)

        else:
            while not stack.isEmpty() and prec[token] < prec[stack.peek()]:
                output.append(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        output.insert(0, stack.pop())

    return " ".join(output)


def prefixEval(prefixExpr):
    operandStack = Stack()
    tokenList = prefixExpr.split()



    for token in tokenList[::-1]:

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

infix = input("\nEnter an infix expression: \n'separate between each element with space'\n")
prefix = inToPre(infix)
print("equivalent prefix: \n", prefix)
print("Result of evaluation: \n", prefixEval(prefix))