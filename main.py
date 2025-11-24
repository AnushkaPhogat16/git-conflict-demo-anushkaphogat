# main.py
def calculate(a, b, op):
    """
    Basic calculator function.
    op: '+', '-', '*', '/'
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else None
    else:
        return None

if __name__ == "__main__":
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Enter operation (+ - * /): ")
    result = calculate(x, y, op)
    print("Result:", result)
