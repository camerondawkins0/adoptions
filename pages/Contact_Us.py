import streamlit as st
import os

from dotenv import load_dotenv
import sqlite3

# Load environment variables from .env file
load_dotenv()

# Create response form
with st.form("Response Form"):
    name = st.text_input("Name")
    cat_of_interest = st.text_input("Cat of Interest")
    contact_info = st.text_input("Contact info (Email or Phone Number)")
    inquiry = st.text_area("Questions or Concerns?")

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

    # Insert response into database when form is submitted
    if submit_button:
        pass
        # Connect to the SQLite database
        # conn = sqlite3.connect('database.db')
        # c = conn.cursor()

        # # Create table if it doesn't exist
        # c.execute('''CREATE TABLE IF NOT EXISTS responses
        #              (name TEXT, cat_of_interest TEXT, contact_info TEXT)''')

        # # Insert response into the table
        # c.execute("INSERT INTO responses VALUES (?, ?, ?)", (name, cat_of_interest, contact_info))

        # # Commit the changes and close the connection
        # conn.commit()
        # conn.close()