n = int(input("Enter the number:"))

reverse_input = str(n)[::-1]

if str(n) == reverse_input:
    print("The number is palindrome")
else:
    print("The number is not palindrome")   