def compute_power(a, b):
    return a ** b

def main():
    try:
        a = int(input("Enter a value for 'a' (between 1 and 10): "))
        b = int(input("Enter a value for 'b' (between 1 and 5): "))
        
        if 1 <= a <= 10 and 1 <= b <= 5:
            result = compute_power(a, b)
            print(f"{a} ^ {b} = {result}")
        else:
            print("Both 'a' and 'b' should be within the specified ranges.")
    except ValueError:
        print("Please enter valid integer values for 'a' and 'b'.")

if __name__ == "__main__":
    main()
