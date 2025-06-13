def balance_check(s: str) -> bool:

    # Needs to be even to be balanced
    if(len(s) % 2 != 0):
        return False
    
    check_stack = []
    open_paren = ['[', '{', '(']

    for i in s:
        if(i in open_paren):
            check_stack.append(i)
        else:
            if(i == ']' and check_stack.pop() != '['):
                return False
            if(i == '}' and check_stack.pop() != '{'):
                return False
            if(i == ')' and check_stack.pop() != '('):
                return False

    return True

print(balance_check('[]'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))
print(balance_check('[[[]])]'))
print(balance_check('[](){([[[]]])}('))
print(balance_check('[{{{(())}}}]((()))'))