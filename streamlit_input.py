import streamlit as st

# Get the current credentials
# session = get_active_session()
st.write(session)
st.divider()

# Get query params from URL
query_params = st.experimental_get_query_params()
# st.write(query_params)

gid = query_params.get("gid", [""])[0]  # Default to empty string if not found

# """
# >> http://localhost:8501/?show_map=True&selected=asia&selected=america.
# >> st.experimental_get_query_params()
# >> {"show_map": ["True"], "selected": ["asia", "america"]

# st.query_params can be used with both key and attribute notation. For example, st.query_params.my_key and st.query_params["my_key"]. All keys and
# values will be set and returned as strings. When you write to st.query_params, key-value pair prefixed with ? is added to the end of your app's 
# URL. Each additional pair is prefixed with & instead of ?. Query parameters are cleared when navigating between pages in a multipage app.

# """

if gid:
    st.write(f'''
    
    GID: {gid}
    
    ''')


    # Fetch and display your time series data based on GUID
else:
    st.write("GID not provided")
