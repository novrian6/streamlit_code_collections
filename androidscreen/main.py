import streamlit as st

def main():
    st.title("Login Screen")

    # Logo or Header
    st.image("android_logo.png", width=200)
    st.write("Welcome to the Login Screen")

    # Form to enter username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Button to submit the form
    if st.button("Login"):
        # Check if the username and password are correct
        if username == "admin" and password == "password":
            st.success("Login successful!")
            st.write("Welcome, " + username + "!")
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
