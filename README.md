## AI-ETL-LLM: AI-Powered ETL & Machine Learning Pipeline  

## Overview

This project is a fully automated AI-powered ETL (Extract, Transform, Load) pipeline that processes data from different sources, applies machine learning models, and provides AI-driven insights via an interactive chatbot.  

## The system:  
- Extracts data from MySQL, MongoDB, and APIs
  
- Cleans & processes data using Pandas & NumPy

- Loads processed data back into MySQL & MongoDB

- Trains a machine learning model for predictive insights

- Offers an AI chatbot (GPT-3.5 Turbo) for data analysis

- Provides a FastAPI-powered API for model predictions

- Includes a Streamlit dashboard for easy visualization

## Installation & Setup  

1. Clone the Repository

  git clone https://github.com/molik-sareen/AI-ETL-LLM.git
  
  cd AI-ETL-LLM

2. Set Up a Virtual Environment

      python -m venv venv
  
      source venv/bin/activate   # For Mac/Linux
  
      venv\Scripts\activate      # For Windows

3. Install Dependencies

      pip install -r requirements.txt

4. Configure Environment Variables

      MYSQL_HOST=your_host
      
      MYSQL_USER=your_user
      
      MYSQL_PASS=your_password
      
      MYSQL_DB=your_db
      
      MONGO_URI=your_mongo_connection_string
      
      MONGO_DB=your_mongo_database
      
      OPENAI_API_KEY=your_openai_api_key

# How to Run the Project?

**Step 1:** Extract, Transform & Load Data

      python src/extract.py
      
      python src/transform.py
      
      python src/load.py

**Step 2:** Train the Machine Learning Model

      python src/ml_model.py

**Step 3:** Chat with the AI Chatbot

      python src/chatbot.py

**Example Prompt:**

    **User:** What insights can I get from this dataset?
    
    **AI:** Based on the dataset, we can analyze trends and predict future values using machine learning.

**Step 4:** Start the API for Model Predictions

      uvicorn src.api:app --reload

      **Open in browser:** http://127.0.0.1:8000/predict/5.0

**Step 5:** View the Dashboard

      streamlit run src/dashboard.py
      
      **Open in browser:** http://localhost:8501

## Technologies Used:

  - Python
  - MySQL & MongoDB (Databases for structured & unstructured data)
  - Pandas & NumPy (Data Cleaning & Processing)
  - Scikit-learn (Machine Learning Model)
  - FastAPI (Backend API)
  - OpenAI GPT-3.5 Turbo (AI Chatbot)
  - Streamlit (Dashboard for visualization)
