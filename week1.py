# Basic Calculator Program
print("********* Simple Calculator *********")

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
op = input("Enter the operation to perform (+,-,*,/,%,//,**): ")

if op == '+':
    ans = x + y
    print(x, op, y, " = ", ans)
elif op == '-':
    ans = x - y
    print(x, op, y, " = ", ans)
elif op == '*':
    ans = x * y
    print(x, op, y, " = ", ans)
elif op == '/':
    if y != 0:
        ans = x / y
        print(x, op, y, " = ", ans)
    else:
        print("Division by zero impossible!!")
elif op == '%':
    ans = x % y
    print(x, op, y, " = ", ans)
elif op == '//':
    ans = x // y
    print(x, op, y, " = ", ans)
elif op == '**':
    ans = x ** y
    print(x, op, y, " = ", ans)
else:
    print("Choose among the options in parenthesis!!")