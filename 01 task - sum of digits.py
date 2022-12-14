number = int(input('введите число, и я выведу сумму его цифр: '))


def DigitsSum(num):
    amount = 0
    while num > 0:
        lastDigit = num % 10
        amount += lastDigit
        num //= 10
    return amount


print(f"Сумма всех цифр в числе => {DigitsSum(number)}")
