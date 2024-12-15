# hack-thamizhagam-hackaton
#

**Overview**
This project is a Streamlit-based web application designed to provide users with automated data preprocessing, interactive visualizations, and a chatbot powered by the LLaMA model (via Groq API). The application simplifies the process of analyzing datasets and extracting meaningful insights, catering to users from diverse industries.

**Features**
Dataset Upload: Upload CSV or Excel files for analysis.
Automated Preprocessing: Handles missing values using forward filling and prepares the dataset for analysis.

**Data Chatbot:**
Powered by the LLaMA model via the Groq API.
Users can ask questions about their data and receive insightful answers.

**Interactive Visualizations:**
Line charts for numerical trends.
Bar charts for categorical distributions.
Insights Generation: Provides key insights based on uploaded datasets.

**Installationv
Follow these steps to set up the project:
Prerequisites
Python 3.8 or later.
Install dependencies listed in requirements.txt.
Steps

Clone the repository:
git clone <repository-url>
cd <repository-folder>

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py

Open the provided URL in a web browser.

Usage
Upload Dataset:
Click on the "Upload Your Dataset" section.
Upload a CSV or Excel file.

Preprocessing:
The application will preprocess the dataset automatically and display a success message.

Ask Questions:
Select the "Ask a Question" option.
Input a query in natural language about your dataset.
View the chatbot’s response.

View Visualizations:
Select the "View Visualizations" option.
Explore automatically generated visualizations.

Gain Insights:
Review key insights generated based on your data.

Dependencies

Streamlit: For creating the web application.

Pandas: For data manipulation and preprocessing.

NumPy: For numerical computations.

Plotly: For interactive visualizations.

Requests: For Groq API integration.

Groq: For interacting with the LLaMA model.

File Structure

project-folder/
|— app.py               # Main application script.
|— requirements.txt    # Dependency file.
|— README.md           # Project documentation.

Example Queries for Chatbot

"What are the trends in my data?"

"Which category has the highest value?"

"What is the average of this column?"
