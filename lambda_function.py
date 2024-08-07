import json
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os
from queries import WIN_RATE_QUERY, PITCH_RATE_QUERY
from decimal import Decimal

# Load environment variables from .env file
load_dotenv()

# Function to get Snowflake credentials from environment variables
def get_snowflake_credentials():
    return {
        "user": os.getenv("USER"),
        "password": os.getenv("PASSWORD"),
        "account": os.getenv("ACCOUNT"),
    }

# Function to handle Decimal conversion
def convert_decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

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
    df = pd.DataFrame(data, columns=columns)
    return df.applymap(lambda x: float(x) if isinstance(x, Decimal) else x).to_dict()  # Convert Decimal to float

# Lambda handler function
def lambda_handler(event, context):
    try:
        # Retrieve Snowflake credentials
        credentials = get_snowflake_credentials()

        # Run queries and get results
        win_rate_df = get_data_from_query(credentials, WIN_RATE_QUERY)
        pitch_rate_df = get_data_from_query(credentials, PITCH_RATE_QUERY)

        # Format the results into a response
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "win_rate": win_rate_df,
                "pitch_rate": pitch_rate_df
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }

        return response

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }
