# Global variable
x = 300

print("Global value is:", x)
print("Enter numbers separated by spaces to find the closest to", x)

# User input
user_input = input("Enter numbers: ")

# Convert input into a list of floats
numbers = list(map(float, user_input.split()))

# Find the number closest to x
closest = min(numbers, key=lambda num: abs(num - x))

print("The number closest to", x, "is:", closest)