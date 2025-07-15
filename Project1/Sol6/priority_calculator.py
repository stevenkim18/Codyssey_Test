def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero.")
    return a / b

def parse_expression(expression: str) -> tuple[list[float], list[str]]:
    tokens: list[str] = expression.split()
    numbers: list[float] = []
    operators: list[str] = []
    
    for i, token in enumerate(tokens):
        if i % 2 == 0:
            try:
                numbers.append(float(token))
            except ValueError:
                raise ValueError("Invalid input.")
        else: 
            if token in ['+', '-', '*', '/']:
                operators.append(token)
            else:
                raise ValueError("Invalid input.")
    
    if len(numbers) != len(operators) + 1:
        raise ValueError("Invalid input.")
    
    return numbers, operators

def calculate_with_priority(numbers: list[float], operators: list[str]):
    nums = numbers[:]
    ops = operators[:]
    
    i = 0
    while i < len(ops):
        if ops[i] == '*':
            result = multiply(nums[i], nums[i + 1])
            nums = nums[:i] + [result] + nums[i + 2:]
            ops = ops[:i] + ops[i + 1:]
        elif ops[i] == '/':
            result = divide(nums[i], nums[i + 1])
            nums = nums[:i] + [result] + nums[i + 2:]
            ops = ops[:i] + ops[i + 1:]
        else:
            i += 1
    
    i = 0
    while i < len(ops):
        if ops[i] == '+':
            result = add(nums[i], nums[i + 1])
            nums = nums[:i] + [result] + nums[i + 2:]
            ops = ops[:i] + ops[i + 1:]
        elif ops[i] == '-':
            result = subtract(nums[i], nums[i + 1])
            nums = nums[:i] + [result] + nums[i + 2:]
            ops = ops[:i] + ops[i + 1:]
        else:
            i += 1
    
    return nums[0]

def main():
    try:
        expression: str = input("수식을 입력하세요: ")
        numbers, operators = parse_expression(expression)
        result = calculate_with_priority(numbers, operators)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError:
        print("Invalid input.")
    except Exception:
        print("Invalid input.")

if __name__ == "__main__":
    main()