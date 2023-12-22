[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10438457&assignment_repo_type=AssignmentRepo)
Project Instructions
==============================

This repo contains the instructions for a machine learning project.

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for describing highlights for using this ML project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │   └── README.md      <- Youtube Video Link
    │   └── final_project_report <- final report .pdf format and supporting files
    │   └── presentation   <-  final power point presentation 
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
       ├── __init__.py    <- Makes src a Python module
       │
       ├── preprocessing data           <- Scripts to download or generate data and pre-process the data
       │   └── make_dataset.py
       │   └── pre-processing.py
       │
       ├── features       <- Scripts to turn raw data into features for modeling
       │   └── build_features.py 
       │   └── balance_data.py
       │   └── correlation.py
       │
       ├── models         <- Scripts to train models and then use trained models to make
       │   │                 predictions
       │   ├── predict_model.py
       │   └── train_model.py
       │
       └── visualization  <- Scripts to create exploratory and results oriented visualizations
           └── visualize.py           

Abstract
------------

Diabetes causes significant impacts on individuals and healthcare systems making it one of the most prevalent chronic illnesses worldwide. While cases of diabetes are inevitable, early detection and prevention of the diseases are crucial for improving outcomes and reducing healthcare costs. 

In the bioinformatics field, machine learning has emerged as a favourable tool for predicting the onset of these diseases based on numerous health and demographic variables. 

Our research aims to analyze a wide range of variables such as cholesterol level, BMI, Blood Pressure, Alcohol consumption, eating habits and many more to identify key trends and patterns that correlate with the disease. We also trained, developed, and deployed cutting edge machine learning models such as logistic regression, XGboosting, Support-Vector Machines, and K-Nearest Neighbors’ in order to predict the onset signs of diabetes.

Overall, our study demonstrates the potential of how statistics and machine learning could be incorporated within the healthcare industry, which could inform premature treatment to improve patient results and reduce healthcare costs.

