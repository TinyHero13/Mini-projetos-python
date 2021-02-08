def convertBinary(n):
    if n > 1:
        convertBinary(n//2)
    print(n % 2, end='')


convertBinary(int(input("Enther the number you want to transform to binary: ")))