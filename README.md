# 📱 SMS Spam Detection using Machine Learning

## 📌 Overview
This project is a **Machine Learning-based SMS Spam Detection System** developed using the **SMS Spam Collection Dataset**. The model classifies SMS messages as **Spam** or **Ham (Legitimate)** by applying Natural Language Processing (NLP) techniques and multiple Machine Learning algorithms.

## 🌐 Live Demo
🔗 **Deployed Application:** https://sms-spam-detector-ml.streamlit.app/

## 🎯 Features
The system performs the following tasks:

- Detects whether an SMS message is **Spam** or **Ham**
- Cleans and preprocesses SMS text
- Removes stopwords and punctuation
- Applies stemming using Porter Stemmer
- Converts text into numerical features using TF-IDF Vectorization
- Predicts SMS messages using a trained Machine Learning model
- Provides instant prediction through a user-friendly Streamlit web application

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- NLTK (Natural Language Toolkit)
- Matplotlib
- Seaborn
- WordCloud
- Streamlit
- Pickle

## 🔄 Project Workflow

- Imported the required Python libraries
- Loaded and explored the SMS Spam Collection dataset
- Performed data cleaning by removing unnecessary columns, handling duplicates, and encoding labels
- Conducted Exploratory Data Analysis (EDA) using visualizations
- Preprocessed SMS messages through:
  - Lowercase conversion
  - Tokenization
  - Removal of stopwords and punctuation
  - Stemming
- Converted text into numerical features using **TF-IDF Vectorization**
- Split the dataset into training and testing sets
- Trained and evaluated multiple Machine Learning algorithms, including:
  - Gaussian Naive Bayes
  - Multinomial Naive Bayes
  - Bernoulli Naive Bayes
  - Support Vector Classifier (SVC)
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - K-Nearest Neighbors
  - AdaBoost
  - Bagging Classifier
  - Extra Trees Classifier
  - Gradient Boosting
  - XGBoost
- Compared model performance using Accuracy and Precision
- Applied ensemble learning techniques:
  - Voting Classifier
  - Stacking Classifier
- Saved the trained model and TF-IDF vectorizer using Pickle
- Built and deployed the application using Streamlit

## 📊 Learning Outcomes

This project helped me understand the complete NLP and Machine Learning workflow, including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Text Preprocessing
- Feature Engineering
- TF-IDF Vectorization
- Model Training
- Model Evaluation
- Model Comparison
- Ensemble Learning
- Model Deployment using Streamlit

## 🚀 Future Enhancements
- Add multilingual SMS spam detection support.
