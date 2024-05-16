import streamlit as st

# Title of the web app
st.title('Simple Calculator')

# Function to perform addition
def add_numbers(num1, num2):
    return num1 + num2

# User input for numbers
num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

# Button to trigger calculation
if st.button('Add'):
    result = add_numbers(num1, num2)
    st.write('The result is:', result)
