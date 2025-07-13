def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero.")
        exit(0)
    return a / b

def input_numbers():
    user_input = input("Enter expression: ")
    list = user_input.split()
    
    if not (2 <= len(list) <= 3):
        print("2~3개 숫자나 연산자를 입력해주세요!")
        return
        
    if len(list) == 2:
        try:
            num1 = float(list[0])
            num2 = float(list[1])
        except ValueError:
            print("첫번쨰 두번째 모두 실수여야 합니다. ex) 10 2")
            return
        
        operator = input("operator(+ - * /): ")
        
        if not (operator in ('+', '-', '*', '/')):
            print("Invalid operator. (+ - * / 중에 하나를 입력해주세요)")
    
        calc(operator, num1, num2)
    else:
        operator = list[1]
        
        if not (operator in ('+', '-', '*', '/')):
            print("Invalid operator. (2번쨰, + - * / 중에 하나를 입력해주세요)")
            return
        
        try:
            num1 = float(list[0])
            num2 = float(list[2])
        except ValueError:
            print("첫번쨰 두번째 모두 실수여야 합니다. ex) 10 2")
        
        calc(operator, num1, num2)

def calc(op, a, b):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    func = operations.get(op)
    
    print(func(a, b))
    
    
def main():
    input_numbers()

if __name__ == "__main__":
    main()