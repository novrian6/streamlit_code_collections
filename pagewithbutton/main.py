import streamlit as st

def main():
    st.title("Button Demo")
    
    # Button to trigger action
    if st.button("Click Me!"):
        # Display text
        st.write("You clicked the button!")
        
        # Display image
        st.image("https://img.freepik.com/free-photo/little-grey-kitten-with-blue-eyes-lies-grey-couch_8353-7261.jpg?w=1800&t=st=1710503094~exp=1710503694~hmac=4f4fefcaffcacf5aef215d20f451a6fc0de71b86d5b68e6de863404af6a66f28", caption="Cute Kitten", use_column_width=True)

if __name__ == "__main__":
    main()
