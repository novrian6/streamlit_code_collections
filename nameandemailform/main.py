import streamlit as st

def main():
    st.title("Name and Email Form")

    # Form to enter name and email
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")

    # Button to submit the form
    if st.button("Submit"):
        # Display the entered name and email
        st.write("Name:", name)
        st.write("Email:", email)

if __name__ == "__main__":
    main()
