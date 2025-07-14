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

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def main():
    try:
        numbers = get_numbers()
    except ValueError as e:
        print(e)
        return 
        
    sorted_numbers = bubble_sort(numbers)
    print("Sorted:", sorted_numbers)

if __name__ == "__main__":
    main()

