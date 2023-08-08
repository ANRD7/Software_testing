a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))

def check_range(a,b):
    if a>15 and b>5:
        print("Both not in range")
    elif a not in range(16):
        print("A not in range")
    elif b not in range(6):
        print("B not in range")
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
