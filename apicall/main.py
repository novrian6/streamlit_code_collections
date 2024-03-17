import streamlit as st
import requests

def fetch_data():
    # URL of the API
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error("An error occurred while fetching data:", e)
        return None

def main():
    st.title("API Data Display")

    # Fetch data from the API
    data = fetch_data()

    # Display the fetched data
    if data:
        st.write("Fetched Data:")
        st.write(data)

if __name__ == "__main__":
    main()
