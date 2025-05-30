# DSA 210 Term Project  
## Predicting Football Match Outcomes Using Betting Odds and Elo Ratings  

This project explores the extent to which football match outcomes can be predicted using pre-match betting odds and Elo ratings. Through a combination of statistical analysis and machine learning, the study aims to evaluate the efficiency of betting markets and quantify the added value of team performance metrics.

---

##  Project Objectives

- Assess the predictive power of implied probabilities derived from betting odds.
- Integrate Elo ratings to capture relative team strength.
- Develop and evaluate a classification model to forecast match results.

---

## Dataset Description

The dataset includes:
- Match results (`FTR`: Home win, Draw, Away win)
- Implied probabilities (`ProbH`, `ProbD`, `ProbA`)
- Team Elo ratings (`HomeElo`, `AwayElo`)
- Derived feature: `EloDiff = HomeElo - AwayElo`

Data was collected and cleaned to ensure consistency, with conversions applied to standardize formats and remove anomalies.

---

##  Methodology

### 1. Data Preprocessing
- Conversion of raw betting odds to implied probabilities.
- Cleaning missing or inconsistent records.
- Generation of Elo-based features to reflect competitive dynamics.

### 2. Exploratory Data Analysis (EDA)
- Distribution of match outcomes and betting probabilities.
- Relationship between Elo differences and outcome likelihood.
- Statistical testing to evaluate market efficiency (binomial hypothesis test).

### 3. Model Development
- **Model used:** Random Forest Classifier
- **Input features:** ProbH, ProbD, ProbA, EloDiff, HomeElo, AwayElo
- **Output:** FTR (match result classification)
- Performance metrics include accuracy, precision, recall, and confusion matrix analysis.

### 4. Feature Importance
- Analysis of which features most influenced model predictions.
- Visualization of importance scores to interpret model decisions.

---

##  Results Summary

- Model achieved an **accuracy of ~44%** on the test set.
- Feature importance showed **ProbH**, `EloDiff`, and `ProbA` were key predictors.
- Betting odds alone provided a strong signal, and Elo ratings contributed to measurable improvement in classification performance.

---

## Technologies Used

- **Language:** Python
- **Libraries:** pandas, numpy, scikit-learn, matplotlib, seaborn
- **Platform:** Jupyter Notebook, GitHub

---

##  How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt


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
