import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.svm import SVC

df = pd.read_csv("D:\\IA_UFCG\\heart_disease_final.csv")
df['target'] = df['target'].apply(lambda x: 0 if x == 0 else 1)
X = df.drop(columns=['target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.30, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

svm_rbf = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale",
    probability=True,
    random_state=42
)

svm_rbf.fit(X_train_scaled, y_train)

joblib.dump(svm_rbf, "../models/svm_rbf_model.pkl")
joblib.dump(scaler, "../models/scaler.pkl")
joblib.dump(X.columns.tolist(), "../models/features.pkl")
