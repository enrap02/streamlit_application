import streamlit as st

# Get query params from URL
query_params = st.query_params()
guid = query_params.get("guid", [""])[0]  # Default to empty string if not found

if guid:
    st.write(f"GUID: {guid}")
    # Fetch and display your time series data based on GUID
else:
    st.write("GUID not provided")
