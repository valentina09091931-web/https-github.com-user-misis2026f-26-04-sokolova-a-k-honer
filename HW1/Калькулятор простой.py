def calculator():
    print("Простой калькулятор. Введите 'exit' для выхода.")
    
    while True:
        op = input("\nВыберите операцию (+, -, *, /, **): ").strip()
        if op.lower() == 'exit':
            print("Выход из программы.")
            break
            
        if op not in ('+', '-', '*', '/', '**'):
            print("Ошибка: неизвестная операция.")
            continue
            
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно вводить только числа.")
            continue

        if op == '+':
            print(f"Результат: {num1 + num2}")
        elif op == '-':
            print(f"Результат: {num1 - num2}")
        elif op == '*':
            print(f"Результат: {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("Ошибка: делить на ноль нельзя!")
            else:
                print(f"Результат: {num1 / num2}")
        elif op == '**':
            print(f"Результат: {num1 ** num2}")

if __name__ == "__main__":
    calculator()
