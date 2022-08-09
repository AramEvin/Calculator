"""Program make a simple calculator"""


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

def exponentiation(x, y):
    return x ** y

def floor_division(x, y):
    return x // y

print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus 6.Exponentiation 7.Floor division")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))

        elif choice == '3':
            print(multiply(num1, num2))

        elif choice == '4':
            print(divide(num1, num2))

        elif choice == '5':
            print(modulus(num1, num2))

        elif choice == '6':
            print(exponentiation(num1, num2))
            
        elif choice == '7':
            print(floor_division(num1, num2))
            
        exit = input("Do you want exit calculation? (yes/no): ")
        if exit == "yes":
          break    
    
    else:
        print("Syntax Error")

#Mika Vorahan em exel