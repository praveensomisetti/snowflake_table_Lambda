import streamlit as st
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os
from queries import WIN_RATE_QUERY, PITCH_RATE_QUERY

# Load environment variables from .env file
load_dotenv()

# Function to get Snowflake credentials from environment variables
def get_snowflake_credentials():
    return {
        "user": os.getenv("USER"),
        "password": os.getenv("PASSWORD"),
        "account": os.getenv("ACCOUNT"),
    }

# Function to get data from Snowflake using a query
def get_data_from_query(credentials, query):
    conn = snowflake.connector.connect(
        user=credentials['user'],
        password=credentials['password'],
        account=credentials['account']
    )
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    columns = [col[0] for col in cur.description]  # Fetch column names
    cur.close()
    conn.close()
    return pd.DataFrame(data, columns=columns)

# Streamlit application
def main():
    st.set_page_config(layout="wide")  # Set page layout to wide

    st.title('Recommendation Performance Metrics')

    # Retrieve Snowflake credentials
    credentials = get_snowflake_credentials()

    # Run queries and get results
    win_rate_df = get_data_from_query(credentials, WIN_RATE_QUERY)
    pitch_rate_df = get_data_from_query(credentials, PITCH_RATE_QUERY)

    # Display Query 1 results on top
    st.header('Recommended vs Non Recommended - Win Rate')
    st.dataframe(win_rate_df, height=10, use_container_width=True)  # Adjust height and use full container width

    # Display Query 2 results below
    st.header('Recommended vs Non Recommended - Pitch Rate')
    st.dataframe(pitch_rate_df, height=10, use_container_width=True)  # Adjust height and use full container width

if __name__ == "__main__":
    main()