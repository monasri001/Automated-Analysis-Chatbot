import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
from groq import Groq
import os

# Streamlit app header
st.set_page_config(
    page_title="Automated Data Analysis Chatbot",
    page_icon="📊",
    layout="centered"  # Enhanced UI with wide layout
)

# Access the API key from environment variables
api = os.getenv("GROQ_API_KEY")
if not api:
    st.error("API key not found. Please set the 'GROQ_API_KEY' environment variable.")
else:
    client = Groq(api_key=api)

# Dataset Upload
st.title("Data Analytics Dashboard")
st.subheader("Upload Your Dataset")
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    st.info("Preprocessing your dataset to get the optimal solution...")

    # Load Dataset
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Preprocessing
    missing_values = df.isnull().sum()
    df.fillna(method='ffill', inplace=True)

    st.success("Preprocessing completed.")

    # Chatbot or Visualization Selection
    st.subheader("Choose Your Action")
    action = st.radio("What would you like to do?", ("Ask a Question", "View Visualizations"))

    if action == "Ask a Question":
        st.subheader("Chat with Your Data")
        st.markdown("Ask questions like:")
        st.markdown("- What are the trends in my data?")
        st.markdown("- Which category has the highest value?")

        question = st.text_input("Ask a question about your data:")

        def query_groq_api(question, dataset):
            """Call Groq API for answering questions."""
            user_message = (
                "You are a data analysis assistant capable of understanding tabular datasets and providing clear, insightful responses to user queries. Your role is to analyze data, identify trends, and answer questions about the dataset accurately and informatively."
                f" Answer the following question based on the dataset: {question}"
                f"interact with these dataset {uploaded_file} and answer related to this dataset alone "
            )
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_message,
                    }
                ],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content

        if st.button("Ask") and question:
            with st.spinner("Fetching answer..."):
                answer = query_groq_api(question, df)
            st.success("Chatbot Response:")
            st.write(answer)

    elif action == "View Visualizations":
        st.subheader("Visualizations")

        # Detect Numerical Columns for Generic Trend Visualization
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) > 0:
            st.write("Numeric Column Visualizations:")
            for column in numeric_columns:
                fig = px.line(df, y=column, title=f"Trend of {column}")
                st.plotly_chart(fig)

        # Detect Categorical Columns for Distribution Visualization
        categorical_columns = df.select_dtypes(include=['object']).columns
        if len(categorical_columns) > 0:
            st.write("Categorical Column Visualizations:")
            for column in categorical_columns:
                value_counts = df[column].value_counts()
                fig = px.bar(value_counts, x=value_counts.index, y=value_counts.values, title=f"Distribution of {column}")
                st.plotly_chart(fig)

        # Insights Section
        st.subheader("Key Insights")
        st.write("Based on the uploaded data, here are some generic insights:")
        if len(numeric_columns) > 0:
            for column in numeric_columns:
                st.write(f"- The average value in column '{column}' is {df[column].mean():.2f}.")
        if len(categorical_columns) > 0:
            for column in categorical_columns:
                top_category = df[column].value_counts().idxmax()
                st.write(f"- The most common category in '{column}' is '{top_category}'.")

else:
    st.warning("Please upload a dataset to proceed.")
