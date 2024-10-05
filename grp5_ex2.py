def arithmetic_operations(num1, num2):
    try:
        print(f"Addition: {num1} + {num2} = {num1 + num2}")
        print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
        print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

        # Handle division and modulus by zero
        if num2 != 0:
            print(f"Division: {num1} / {num2} = {num1 / num2}")
            print(f"Modulus: {num1} % {num2} = {num1 % num2}")
        else:
            print("Division and modulus by zero are not defined.")
        
        print(f"Exponent: {num1} ** {num2} = {num1 ** num2}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
int_num1 = 10       # int
int_num2 = 3        # int
float_num1 = 10.5   # float
float_num2 = 2.5    # float
complex_num1 = 2 + 3j  # complex
complex_num2 = 1 + 4j  # complex

print("Integer Operations:")
arithmetic_operations(int_num1, int_num2)

print("\nFloat Operations:")
arithmetic_operations(float_num1, float_num2)

print("\nComplex Operations:")
arithmetic_operations(complex_num1, complex_num2)

# Variable Assignment
num1 = 25000000        # Without underscores
num2 = 25_000_000      # With underscores
print("\nVariable Assignment:")
print(num1)
print(float_2)

# Creating variables and checking types
int_var = 10               # Integer
float_var = 10.5          # Float
complex_var = 2 + 3j      # Complex

print("\nType Checking:")
print(f"int_var: {int_var}, Type: {type(int_var)}")
print(f"float_var: {float_var}, Type: {type(float_var)}")
print(f"complex_var: {complex_var}, Type: {type(complex_var)}")
