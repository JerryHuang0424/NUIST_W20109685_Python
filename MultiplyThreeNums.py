def multiply_three_numbers(num1, num2, num3):
    return num1 * num2 * num3

def main():
    # Input: Get three numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        # Calculate the product
        product = multiply_three_numbers(num1, num2, num3)
        
        # Output: Display the result
        print(f"The product of {num1}, {num2}, and {num3} is: {product}")
    
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
