# Initialize the result to 0; this will store the result of calculations
result = 0

# Initialize 'operand' to None; this will store the last number entered
operand = None

# Initialize 'operator' to None; this will store the operator (+, -, *, /)
operator = None

# Initialize 'wait_for_number' to True; this is a flag that indicates whether the program is waiting for a number or an operator
wait_for_number = True

# Start an infinite loop to continuously interact with the user
while True:
    # Get user input and display a prompt ">>> "
    response = input(">>> ")

    # Attempt to execute the following code, and handle exceptions
    try:
        # Check if the program is currently waiting for a number
        if wait_for_number:
            # Split the user's input by the dot (.) to check for decimal numbers
            parts = response.split(".")

            # Define an error message for non-numeric input
            err_msg = f"'{response}' is not a number. Try again."

            # If there are more than two parts (more than one dot), raise an exception
            if len(parts) > 2:
                raise ValueError(err_msg)

            # Iterate through each part and check if it's numeric
            for part in parts:
                if not part.isnumeric():
                    raise ValueError(err_msg)

            # If there's only one part, convert it to an integer; otherwise, convert it to a float
            if len(parts) == 1:
                operand = int(response)
            else:
                operand = float(response)

            # Perform the operation based on the operator or add the operand to the result
            if operator is None or operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            else:
                result /= operand
        else:
            # If the user input is "=", print the result and exit the loop
            if response == "=":
                print(f"Result: {result}")
                break

            # If the user input is not a valid operator, raise an exception
            if response not in ["+", "-", "*", "/"]:
                raise ValueError(f"{response} is not '+' or '-' or '/' or '*'. Try again")

            # Set the operator based on the user's input
            operator = response

        # Toggle the 'wait_for_number' flag to switch between waiting for an operator and a number
        wait_for_number = not wait_for_number

    except ValueError as e:
        # Handle exceptions by printing an error message
        print(e)