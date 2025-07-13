def get_numbers():
    user_input = input("여러개의 실수를 공백으로 구분하여 입력: ")
    str_numbers = user_input.split()

    if not str_numbers:
        raise ValueError("Invalid input.")

    numbers = []
    for s in str_numbers:
        try:
            num = float(s)
            numbers.append(num)
        except ValueError:
            raise ValueError("Invalid input.")
    
    return numbers

def find_min(numbers):
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

def find_max(numbers):
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

def main():
    try:
        numbers = get_numbers()
        min_val = find_min(numbers)
        max_val = find_max(numbers)
        print(f"Min: {min_val}, Max: {max_val}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()