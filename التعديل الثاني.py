from pythonds import Stack
def p_power_string(mylist,p):
    exp = " "
    for i in range(len(mylist)):
        if  i != len(mylist)-1:
            exp += str(mylist[i]) + " ^ " + str(p) + " + "
        else:
            exp += str(mylist[i]) + " ^ " + str(p)

    return exp


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

print ("\nthe required string is   " ,   p_power_string([1,2,3],5),"\n")
prefix = inToPre(p_power_string([1,2,3],5))
print("equivalent prefix: \n", prefix)
print("Result of evaluation: \n", prefixEval(prefix))