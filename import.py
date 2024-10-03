import math
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
df = pd.read_excel("C:/Users/uongb/Documents/School/Senior/CS105 Final Proj/Predicting-Academic-Success-vs.-Dropout-Rate/CS105 W24 Survey (Responses).xlsx", sheet_name = 'Form Responses 1')

print("Columns in Dataframe:", df.columns)

#only keeping course, nationality, age, gender and grade @ 1st semester
cols_to_keep = ["Course", "Nacionality", "Gender", "Age at enrollment",
                "Curricular units 1st sem (grade)", "Curricular units 2nd sem (grade)",
                "Curricular units 1st sem (enrolled)", "Curricular units 2nd sem (enrolled)"]

df_selected = df[cols_to_keep].copy()

print("Shape: ", df_selected.shape)
df_selected.head()