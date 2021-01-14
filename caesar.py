def convert():
    word = input("Enter the word you want to encrypt: ")
    key = int(input("Enter the key you want: "))
    lst = []
    for i in word:
        lst.append(chr(ord(i) + key))

    string = "".join(lst)
    print(string)


convert()