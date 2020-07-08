# Aim 
The aim of the project is to identify trends in heart data to predict certain cardiovascular events or find any clear indications of heart health. The database is provided by Cleveland and contains 14 attributes.

# Attribute Information:
1) age: age in years
2) sex: sex (1 = male; 0 = female)
3) cp: chest pain type
-- Value 0: typical angina
-- Value 1: atypical angina
-- Value 2: non-anginal pain
-- Value 3: asymptomatic
4) trestbps: resting blood pressure (in mm Hg on admission to the hospital)
5) chol: serum cholestoral in mg/dl
6) fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
7) restecg: resting electrocardiographic results
-- Value 0: normal
-- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
-- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
8) thalach: maximum heart rate achieved
9) exang: exercise induced angina (1 = yes; 0 = no)
10) oldpeak = ST depression induced by exercise relative to rest
11) slope: the slope of the peak exercise ST segment
-- Value 0: upsloping
-- Value 1: flat
-- Value 2: downsloping
12) ca: number of major vessels (0-3) colored by flourosopy
13) thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
14) condition: 0 = no disease, 1 = disease


# Data correlation
Data correlation is the way in which one dataset may correspond to another dataset. In Machine Learning, data correlation demonstrates how system's features correspond with system's output. We use data visualization in order to find how individual features may correlate with the output:

![image](https://user-images.githubusercontent.com/43147324/86821795-81e1b600-c093-11ea-9644-87f6b48d7928.png)


# Model 
A predictive model is developed using Random Forest from scikit learn library. Also, GridSearchCV is used for tuning the hyper-parameters of the estimator which  exhaustively considers all parameter combinations, evaluates them and the best combination is retained. Prediction and evaluation of the model:






# Acknowledgements
Creators:

1) Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
2) University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
3) University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
4) V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.

Donor:
David W. Aha (aha '@' ics.uci.edu) (714) 856-8779


