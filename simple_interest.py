# Simple Interest Calculator in Python

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Taking user input
try:
    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Rate of Interest (in %): "))
    time = float(input("Enter Time (in years): "))

    # Calculate interest
    interest = calculate_simple_interest(principal, rate, time)

    # Display result
    print(f"Simple Interest: {interest:.2f}")

except ValueError:
    print("Invalid input! Please enter numerical values for principal, rate, and time.")
