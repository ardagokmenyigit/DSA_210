# DSA_210
DSA 210 project


# Analyzing the Predictive Power of Betting Odds on Football Match Outcomes

## Overview
This project investigates the relationship between pre-match betting odds and the final outcomes of football matches. The primary goal is to evaluate the accuracy of betting markets in predicting match results and to identify key factors that influence these predictions.

## Motivation
Sports betting markets are renowned for their predictive capabilities, yet their accuracy remains a subject of debate. By comparing pre-match odds with actual match scores, this project aims to:
- Assess the efficiency of betting markets in forecasting game outcomes.
- Understand which factors—such as home advantage and team performance metrics—affect prediction accuracy.
- Provide insights that may benefit sports analysts, bettors, and data science enthusiasts.

## Data Sources
- **Match Scores:** Official match results obtained from reliable football data APIs or league websites.
- **Betting Odds:** Pre-match betting odds collected from sports betting websites or relevant datasets.

## Methodology
1. **Data Collection & Cleaning:**  
   - Gather football match scores and corresponding pre-match betting odds.
   - Clean and preprocess the data to ensure consistency by handling missing values and normalizing odds formats.

2. **Exploratory Data Analysis (EDA):**  
   - Visualize the distribution of odds and match outcomes.
   - Identify trends and patterns in the data through descriptive statistics and visualization techniques.

3. **Statistical Analysis & Machine Learning:**  
   - Perform correlation analysis and statistical tests to examine the relationship between betting odds and match results.
   - Develop regression or classification models to predict match outcomes based on the betting odds.
   - Evaluate model performance using appropriate metrics (e.g., accuracy and mean squared error).

4. **Visualization:**  
   - Create data visualizations (charts and graphs) to clearly present insights.
   - Compare predicted outcomes with actual match results through plots and summary statistics.

## Tools and Technologies
- **Programming Language:** Python
- **Libraries:**  
  - Data manipulation: `pandas`, `numpy`  
  - Machine Learning: `scikit-learn`  
  - Visualization: `matplotlib`


## Usage
- **Data Collection:** Run the script in `data_collection.py` to fetch and store match scores and betting odds.
- **Exploratory Data Analysis:** Open `eda.ipynb` (Jupyter Notebook) to visually explore the data.
- **Model Training & Evaluation:** Execute `model_analysis.py` to train machine learning models and assess their performance.
- **Visualization:** Review the generated plots in the `/figures` directory for insights into the relationship between odds and match outcomes.

## Results
This analysis will reveal:
- The degree to which pre-match betting odds align with actual match outcomes.
- The strengths and limitations of betting markets in predicting game results.
- Key factors that may improve prediction models.

## Future Work
- **Feature Enrichment:** Incorporate additional variables such as team performance statistics, player injuries, or historical trends.
- **Model Enhancement:** Experiment with advanced machine learning models or ensemble techniques.
- **Real-Time Analysis:** Develop a system for real-time predictions as match data and odds become available.
