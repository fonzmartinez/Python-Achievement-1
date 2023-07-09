a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
operator = input("Enter a '+' if you want to add or a '-' if you want to subtract: ")

if operator == "+":
    print("Your numbers added together equal " + str(a + b))

elif operator == "-":
    print("Your numbers subtracted equal " + str(a - b))

else: 
    print("Unknown operator")