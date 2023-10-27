# Define a function called 'operator_checker' that takes an argument 'var'
def operator_checker(var):
    # If 'var' is "=", return None to indicate the end of input
    if var == "=":
        return None

    # If 'var' is not one of the valid operators, raise a ValueError with an error message
    if var not in ["+", "-", "*", "/"]:
        raise ValueError(f"{var} is not '+' or '-' or '/' or '*'. Try again")

    # Return 'var' to indicate a valid operator
    return var

# Define a function called 'number_checker' that takes an argument 'var'
def number_checker(var):
    # Split 'var' by the dot (.) to check for decimal numbers
    parts = var.split(".")

    # Define an error message for non-numeric input
    err_msg = f"'{var}' is not a number. Try again."

    # If there are more than two parts (more than one dot), raise an exception
    if len(parts) > 2:
        raise ValueError(err_msg)

    # Iterate through each part and check if it's numeric
    for part in parts:
        if not part.isnumeric():
            raise ValueError(err_msg)

    # Return 'var' to indicate a valid number
    return var

# Create a dictionary 'checkers' with two functions to check operators and numbers
checkers = {
    True: operator_checker,  # 'True' indicates the need for an operator
    False: number_checker   # 'False' indicates the need for a number
}

# Define a function called 'main' to execute the code
def main():
    # Initialize an empty 'expression' to store the user's input
    expression = ""
    
    # Initialize 'operator' to 'False' to indicate that the first input should be a number
    operator = False
        
    # Start an infinite loop to continuously interact with the user
    while True:
        # Display the current 'expression' to the user
        print(f"Expression: {' '.join(expression)}")

        # Get user input and display a prompt ">>> "
        response = input(">>> ")

        # Attempt to execute the following code, and handle exceptions
        try:
            # Use the appropriate checker function based on the 'operator' flag, and store the result in 'var'
            var = checkers[operator](response)
        except ValueError as err:
            # Handle exceptions by printing an error message and continue the loop
            print(err)
            continue

        # If 'var' is None, it means the user entered "=", so calculate and print the result
        if var is None:
            result = eval(expression)
            print(f"Result: {result}")

            return

        # Append 'var' to the 'expression' and toggle the 'operator' flag
        expression += var
        operator = not operator

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # If it is, call the 'main' function to start the execution
    main()