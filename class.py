import streamlit as st

# Title and Description
st.title("Simple Calculator")
st.write("This is a simple calculator built with Streamlit. Enter two numbers and select an operation.")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0, step=0.1, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, step=0.1, format="%.2f")

# Operation selection
operation = st.selectbox("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on the selected operation
result = None
if st.button("Calculate"):
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
    
    if result is not None:
        st.success(f"The result is: {result}")
