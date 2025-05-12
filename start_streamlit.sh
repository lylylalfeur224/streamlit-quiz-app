#!/bin/bash
# Start Streamlit app and redirect output to a log file

echo "Starting Streamlit app..." > streamlit.log
streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false --server.port 8501 --server.address 0.0.0.0 >> streamlit.log 2>&1
echo "Streamlit app started and logging to streamlit.log"
