# برنامه‌ای برای بررسی عدد اول
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# گرفتن ورودی از کاربر
try:
    num = int(input("یک عدد وارد کنید: "))
    if is_prime(num):
        print(f"{num} یک عدد اول است.")
    else:
        print(f"{num} عدد اول نیست.")
except ValueError:
    print("لطفاً یک عدد صحیح وارد کنید!")
