#!/usr/bin/env python3

import operator
import colored
from colored import fg


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def uncoveredfunction():
    a = 1
    b = 2
    c = a + b 
    return c

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
            print("Result: ", fg(1), result, fg(15))
        else:    
            print("Result: ", result)

if __name__ == '__main__':
    main()
