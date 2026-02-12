# SpaceX Falcon 9 First Stage Landing Prediction

## IBM Data Science Professional Certificate - Applied Data Science Capstone

### Project Overview

SpaceX advertises Falcon 9 rocket launches on its website with a cost of $62 million, while other providers charge upward of $165 million per launch. Much of the savings is because SpaceX can reuse the first stage of the rocket. By predicting whether the first stage will land successfully, we can determine the cost of a launch and provide valuable insights for competing companies bidding against SpaceX.

This capstone project applies the full data science methodology — from data collection and wrangling to exploratory data analysis, interactive visual analytics, and predictive machine learning modeling — to predict whether SpaceX Falcon 9 first-stage boosters will successfully land.

### Key Findings

- **Overall Success Rate:** 67% across 90 Falcon 9 launches (2010–2020)
- **Best Launch Site:** KSC LC-39A achieved the highest success rate
- **Success Trend:** Landing success rates have increased significantly over time, especially after 2015
- **Payload Impact:** Heavier payloads (>6,000 kg) tend to have higher success rates with newer booster versions
- **Best ML Model:** All four models (Logistic Regression, SVM, Decision Tree, KNN) achieved **83.33% test accuracy**; Decision Tree had the best cross-validation score (86.07%)

### Repository Structure

```
├── README.md                                          # Project overview
├── dataset_part_1.csv                                 # Raw SpaceX launch data
├── dataset_part_2.csv                                 # Processed data with Class labels
├── dataset_part_3.csv                                 # One-hot encoded features (83 columns)
├── Spacex.csv                                         # SQL analysis dataset (101 records)
├── SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb # ML prediction models
├── DV0101EN-Final-Assign-Part1-v1.jupyterlite.ipynb   # Data visualization notebook
└── spacex_dash_app.py                                 # Plotly Dash interactive dashboard
```

### Methodology

1. **Data Collection**
   - SpaceX REST API (`api.spacexdata.com/v4`)
   - Wikipedia web scraping with BeautifulSoup

2. **Data Wrangling**
   - Handling missing values (26 missing LandingPad entries)
   - Creating binary `Class` variable from landing outcomes
   - One-hot encoding categorical features (80 columns after encoding)

3. **Exploratory Data Analysis**
   - SQL queries on SQLite database (101 records)
   - Visualization with Matplotlib and Seaborn
   - Scatter plots, bar charts, and line charts

4. **Interactive Visual Analytics**
   - Folium maps with launch site markers and success/failure clustering
   - Plotly Dash dashboard with dropdown filters, pie charts, and payload sliders

5. **Predictive Analysis (Machine Learning)**
   - StandardScaler feature normalization
   - Train/Test split: 80/20 (72 train, 18 test)
   - GridSearchCV with 10-fold cross-validation
   - Models: Logistic Regression, SVM, Decision Tree, KNN

### Machine Learning Results

| Model               | Best CV Score | Test Accuracy | Best Parameters                        |
|---------------------|---------------|---------------|----------------------------------------|
| Logistic Regression | 84.64%        | 83.33%        | C=0.01, penalty=l2, solver=lbfgs       |
| SVM                 | 84.82%        | 83.33%        | kernel=sigmoid, C=1.0, gamma=0.0316    |
| Decision Tree       | 86.07%        | 77.78%        | criterion=gini, max_depth=6, splitter=random |
| KNN                 | 84.82%        | 83.33%        | n_neighbors=10, algorithm=auto, p=2    |

### Technologies Used

- **Languages:** Python 3
- **Libraries:** pandas, NumPy, Matplotlib, Seaborn, Plotly, Folium, scikit-learn, BeautifulSoup, requests
- **Database:** SQLite
- **Tools:** Jupyter Notebook, Plotly Dash

### Author

IBM Data Science Professional Certificate Capstone Project

### License

This project is part of the IBM Data Science Professional Certificate program on Coursera.
