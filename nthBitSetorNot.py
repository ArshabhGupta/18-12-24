def setornot(number, n):
    if number & (1 << (n - 1)):
        print("Set")
    else:
        print("Not Set")

number = int(input("Enter a number: "))
n = int(input("Enter a bit number: "))
setornot(number, n)