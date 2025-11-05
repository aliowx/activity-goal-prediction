# Flight Delay Prediction Project

## Overview

This project implements and evaluates machine learning models for predicting flight delays based on historical flight data. The workflow includes data preprocessing, feature engineering, encoding, model training, hyperparameter tuning, evaluation, and comparison across multiple classifiers.  

The primary goal is to provide **robust predictive models** that can help airlines and passengers anticipate delays and make informed decisions.  

---

## Dataset

- **Features**: Flight schedule information such as departure time, day of the week, carrier, origin, and destination.  
- **Target**: `Flight Status` (Delayed / On-Time).  
- **Train/Test Split**: The dataset is split into 80% training and 20% testing.  
- **Class Distribution**: Approximately 32% of flights are delayed, introducing **moderate class imbalance**.  

---

## Pipeline

1. **Data Loading & Inspection**  
   - Read the dataset and check for missing values.  
   - Identify categorical vs numerical features.  

2. **Feature Encoding**  
   - Applied **ModeDropOneHotEncoder** for categorical variables.  
   - Columns representing the mode of each feature are dropped to reduce redundancy.  
   - Ensured train-test feature alignment to prevent unseen categories in the test set.  

3. **Train-Test Split**  
   - Stratified split to maintain target distribution across train and test sets.  

4. **Models Implemented**  
   - **Decision Tree** (with Cost Complexity Pruning)  
   - **k-NN Classifier**  
   - **Logistic Regression** (with grid search over regularization strength)  

5. **Evaluation Metrics**  
   - **Primary Metric:** Area Under the ROC Curve (AUC)  
   - Handles single-class edge cases safely with a fallback AUC = 0.5.  
   - Includes **leaf-level interpretation** for the Decision Tree model.  
   - Feature importance analysis for interpretability.  

6. **Model Selection**  
   - Robust comparison of models using **Test AUC**.  
   - Safe handling of nan values when the dataset contains only one class.  

---

## Part 5: Why AUC > Accuracy?

AUC (Area Under the ROC Curve) is superior to accuracy in many real-world scenarios, especially for classification tasks with imbalanced classes or differing misclassification costs.  

**Advantages of AUC over Accuracy:**

1. **Class Imbalance**  
   - Accuracy can be misleading if the majority class dominates.  
   - Example: A 68% “On-Time” rate → predicting all flights as on-time gives 68% accuracy but no predictive value.  

2. **False Positives vs False Negatives**  
   - AUC evaluates the ranking of predicted probabilities, not just labels, accounting for different costs of misclassification.  

3. **Threshold-Independent Evaluation**  
   - Accuracy depends on a fixed threshold (e.g., 0.5) to convert probabilities into classes.  
   - AUC assesses model performance across all thresholds, providing a more robust evaluation metric.  

**In this project:**  
- Delay rate = 32% → moderate imbalance.  
- Using AUC ensures a **robust, threshold-independent evaluation** of models.  

---

## Key Insights

- Decision Tree may predict a single class if the dataset is small or highly imbalanced.  
- Logistic Regression provides probability estimates suitable for threshold-independent evaluation.  
- Feature importance analysis highlights the most predictive variables for delays.  
- Top-performing model selection is based on **Test AUC**, not accuracy, ensuring reliability across thresholds.  

---

## Requirements

- Python 3.10+  
- Libraries: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `logging`  

---

## Usage

1. Clone the repository.  
2. Install required packages:  
```bash
python env 
