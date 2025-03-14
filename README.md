# DSA_210
DSA 210 project
OVERVIEW
This project investigates the relationship between pre-match betting odds and the final outcomes of football matches. The goal is to evaluate how well betting markets predict match results and to identify key factors that influence the accuracy of these predictions.
MOTIVATION
Sports betting markets are known for their predictive power, but how accurate are they really? By comparing pre-match odds with actual match scores, this project aims to:
 Assess the efficiency of betting markets in forecasting game outcomes.
 Understand which factors (e.g., home advantage, team performance metrics) affect prediction accuracy.
 Provide insights that could be valuable for sports analysts, bettors, and data science enthusiasts.
 
Data Sources

Match Scores: Official match results obtained from reliable football data APIs or league websites.
Betting Odds: Pre-match betting odds collected from sports betting websites or relevant datasets.
Methodology

Data Collection & Cleaning:
Gather football match scores and corresponding pre-match betting odds.
Clean and preprocess the data to ensure consistency (handling missing values, normalizing odds formats, etc.).

Exploratory Data Analysis (EDA):
Visualize the distribution of odds and match outcomes.
Identify trends and patterns in the data through descriptive statistics and visualization techniques.

Statistical Analysis & Machine Learning:
Perform correlation analysis and statistical tests to determine the relationship between betting odds and match results.
Develop regression or classification models to predict match outcomes based on the betting odds.
Evaluate model performance using appropriate metrics (e.g., accuracy, mean squared error).

Visualization:
Use data visualizations (charts and graphs) to present insights clearly.
Compare predicted outcomes versus actual match results through plots and summary statistics.

Tools and Technologies

Programming Language: Python
Libraries:
Data manipulation: pandas, numpy
Machine Learning: scikit-learn
Visualization: matplotlib

Usage

Data Collection: Run the script in data_collection.py to fetch and store match scores and betting odds.
Exploratory Data Analysis: Execute eda.ipynb (Jupyter Notebook) to explore the data visually.
Model Training & Evaluation: Run model_analysis.py to train machine learning models and evaluate their performance.
Visualization: Check the generated plots in the /figures directory for insights into the relationship between odds and match outcomes.

Results

The analysis will shed light on:

How closely pre-match betting odds align with actual match results.
The strengths and limitations of betting markets in predicting outcomes.
Potential factors that can improve the prediction models.

Future Work

Feature Enrichment: Incorporate additional variables such as team performance statistics, player injuries, or historical trends.
Model Enhancement: Experiment with advanced machine learning models or ensemble techniques.
Real-Time Analysis: Develop a system to perform real-time predictions as match data and odds become available.

