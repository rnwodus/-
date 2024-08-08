import streamlit as st

number = st.number_input(
    "Insert a number", value=None, placeholder="Type a number...", key="number1"
)

number2 = st.number_input(
    "Insert a number", value=None, placeholder="Type a number...", key="number2"
)


option = st.selectbox(
    "How would you like to be contacted?",
    ("+", "*", "-"),
    index=None,
    placeholder="Select contact method...",
)

button = st.button("Button")

if button:
    if option == "+":
        st.write(number+number2)

    if option == "-":
        st.write(number-number2)

    if option == "*":
        st.write(number*number2)
        

st.write("You selected:", option)