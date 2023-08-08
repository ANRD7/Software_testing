a = int(input("Enter value for A (between 1 and 10): "))
b = int(input("Enter value for B (between 1 and 5): "))

def Exponential_range(a,b):
    if a>10 and b>5:
        print("Both NOT in range")
    else:
        if a not in range(11):
            print("A is NOT in range")
        elif b not in range(6):
            print("B is NOT in range")
        else:
            print(a**b)

        
Exponential_range(a,b)
