import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score
from imblearn.over_sampling import SMOTE
import joblib

# 1. Load Dataset
df = pd.read_csv("creditcard.csv")
print("Dataset shape:", df.shape)

# 2. Preprocessing
df['Amount'] = StandardScaler().fit_transform(df[['Amount']])
df = df.drop(['Time'], axis=1)

# 3. Features and Labels
X = df.drop('Class', axis=1)
y = df['Class']

# 4. Train-test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 5. Handle Imbalance using SMOTE
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X_train, y_train)

print("Before SMOTE:", y_train.value_counts())
print("After SMOTE:", y_res.value_counts())

# 6. Train Models

# Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_res, y_res)
lr_pred = lr.predict(X_test)

# Random Forest
rf = RandomForestClassifier(n_estimators=10, max_depth=10, random_state=42)
rf.fit(X_res, y_res)
rf_pred = rf.predict(X_test)

# 7. Evaluation
print("\n=== Logistic Regression ===")
print(confusion_matrix(y_test, lr_pred))
print(classification_report(y_test, lr_pred))
print("AUC Score:", roc_auc_score(y_test, lr.predict_proba(X_test)[:, 1]))

print("\n=== Random Forest ===")
print(confusion_matrix(y_test, rf_pred))
print(classification_report(y_test, rf_pred))
print("AUC Score:", roc_auc_score(y_test, rf.predict_proba(X_test)[:, 1]))

# 8. Save Model
joblib.dump(rf, "model.pkl")
print("Model saved as model.pkl")
