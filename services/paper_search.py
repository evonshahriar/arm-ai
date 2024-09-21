import requests
import streamlit as st

# CrossRef API base URL for works
CROSSREF_API_URL = "https://api.crossref.org/works"

def search_crossref(query):
    try:
        # Define the parameters for the request
        params = {
            'query': query,
            'rows': 10,  # Limit the number of results to 5
            'select': 'title,DOI'  # Specify fields to return (title and DOI)
        }

        # Include your email in the User-Agent header (recommended by CrossRef)
        headers = {
            'User-Agent': 'YourAppName/1.0 (mailto:your.email@example.com)'
        }

        # Send GET request to CrossRef API with headers
        response = requests.get(CROSSREF_API_URL, params=params, headers=headers)

        if response.status_code == 200:
            # Parse the JSON response to extract relevant data
            return response.json().get('message', {}).get('items', [])
        else:
            # Display error if response is not successful
            st.error(f"CrossRef API Error: {response.status_code}")
            return []
    except Exception as e:
        # Handle connection errors
        st.error(f"Error connecting to CrossRef API: {e}")
        return []
