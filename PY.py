import streamlit as st

# Streamlit app title
st.title("Add Two Numbers")

# Input fields for the two numbers
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

# Button to perform addition
if st.button("Add"):
    result = num1 + num2
    st.write(f"The sum of {num1} and {num2} is {result}.")
