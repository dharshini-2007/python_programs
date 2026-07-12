N = int(input("Enter the number:"))

if (N%3 == 0):
    print("Fizz")
elif(N%5 == 0):
    print("Buzz")
elif(N%3 == 0 and N%5 == 0):
    print("FizzBUZZ")
else:
    print(N)        
