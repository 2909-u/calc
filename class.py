import streamlit as st
import math

# Initialize session state for calculation history
if "history" not in st.session_state:
    st.session_state.history = []

# App Title and Description
st.title("Advanced Calculator")
st.write("Perform basic and advanced calculations with this interactive calculator.")

# Input Fields for Numbers
num1 = st.number_input("Enter the first number", value=0.0, step=0.1, format="%.2f")
num2 = st.number_input("Enter the second number (if applicable)", value=0.0, step=0.1, format="%.2f")

# Operation Selection
operation = st.selectbox(
    "Select an operation",
    ("Add", "Subtract", "Multiply", "Divide", "Modulus", "Exponentiation", "Square Root")
)

# Perform Calculation
result = None
if st.button("Calculate"):
    try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed!")
        elif operation == "Modulus":
            if num2 != 0:
                result = num1 % num2
            else:
                st.error("Division by zero is not allowed!")
        elif operation == "Exponentiation":
            result = num1 ** num2
        elif operation == "Square Root":
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                st.error("Square root of a negative number is not defined!")

        if result is not None:
            st.success(f"The result is: {result}")
            # Save to history
            st.session_state.history.append(f"{num1} {operation} {num2} = {result}" if "Square Root" not in operation else f"{operation}({num1}) = {result}")

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display History of Calculations
if st.checkbox("Show Calculation History"):
    if st.session_state.history:
        st.write("### Calculation History:")
        for calc in st.session_state.history:
            st.write(calc)
    else:
        st.info("No calculations performed yet.")

# Clear Inputs Button
if st.button("Clear Inputs"):
    st.session_state.history.clear()
    st.experimental_rerun()

# Footer
st.write("### Features:")
st.write("- Basic operations: Add, Subtract, Multiply, Divide")
st.write("- Advanced operations: Modulus, Exponentiation, Square Root")
st.write("- Persistent history of calculations within the session")
