def generate_password(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result


for n in range(3, 21):
    password = generate_password(n)
while True:
    n = int(input("Введите число от 3 до 20: "))
    if n < 3 or n > 20:
        print("Пожалуйста, введите число от 3 до 20.")
    else:
        result = generate_password(n)
        print(f"Для числа {n} пароль: {result}")
