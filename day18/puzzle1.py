#!/usr/bin/env python3

with open("input", "r") as fileIn:
    expressions = [line.strip() for line in fileIn.readlines()]


def operation(first, second, operator):
    assert operator == "+" or operator == "*"
    if operator == '+':
        return first + second
    else:
        return first * second

def extractor(list_to_parse):
    while len(list_to_parse) > 1:
        num1 = int(list_to_parse.pop())
        operator = list_to_parse.pop()
        num2 = int(list_to_parse.pop())
        result = operation(num1, num2, operator)
        list_to_parse.append(str(result))

    return list_to_parse[0]

def tokenizer(line):
    line = line.replace("(", "( ")
    token_list = line.replace(")", " )")

    tmp_stack = []
    total = 0
    for token in token_list:
        if token.isdigit() or token in ['+', '*', '(']:
            tmp_stack.append(token)
        elif token == ')':
            ordered_stack = []
            while tmp_stack[len(tmp_stack)-1] != '(':
                ordered_stack.append(tmp_stack.pop())
            tmp_stack.pop()
            result = extractor(ordered_stack)
            tmp_stack.append(result)

    tmp_stack.reverse()
    result = extractor(tmp_stack)
    return result

grand_total = 0
for line in expressions:
   grand_total += int(tokenizer(line))

print(grand_total)
