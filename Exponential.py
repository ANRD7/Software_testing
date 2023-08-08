a = int(input("Enter value for A (between 1 and 10): "))
b = int(input("Enter value for B (between 1 and 5): "))

def check_range(a,b):
    if a>15 and b>5:
        print("Both NOT in range")
    elif a not in range(11):
        print("A NOT in range")
    elif b not in range(6):
        print("B NOT in range")
    else:
        Exponential(a,b)


def Exponential(a,b):  
    if a>0 and a<=15:
        if b>0 and b<=5:
            print(a**b,"Exponential Number.")
        else:
            print("Invalid Range of B.")
    else:
        print("Invalid Range of A.")

check_range(a,b)
