import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_score, 
    f1_score, 
    roc_auc_score, 
    roc_curve
)
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

df = pd.read_csv("D:\\IA_UFCG\\heart_disease_final.csv")
df['target'] = df['target'].apply(lambda x: 0 if x == 0 else 1)
X = df.drop(columns=['target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.30, random_state=42)
X_train = pd.DataFrame(X_train, columns=X.columns)
X_test = pd.DataFrame(X_test, columns=X.columns)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

modelos = {
    "Regressão Logística": LogisticRegression(max_iter=2000),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM-RBF": SVC(kernel="rbf", probability=True),
    "Random Forest": RandomForestClassifier(n_estimators=300),
    "XGBoost": XGBClassifier(eval_metric='logloss')
}

usar_scaled = ["Regressão Logística", "KNN", "SVM-RBF"]
resultados = {}
f1s = {}
precisoes = {}
roc_aucs = {}
roc_curves = {}

for nome, modelo in modelos.items():

    print(f"Treinando modelo: {nome}")

    if nome in usar_scaled:
        modelo.fit(X_train_scaled, y_train)
        X_test_input = X_test_scaled
        X_train_input = X_train_scaled
    else:
        modelo.fit(X_train, y_train)
        X_test_input = X_test
        X_train_input = X_train
        
    y_pred = modelo.predict(X_test_input)
    
    if hasattr(modelo, "predict_proba"):
        y_prob = modelo.predict_proba(X_test_input)[:, 1]
    elif hasattr(modelo, "decision_function"):
        y_prob = modelo.decision_function(X_test_input)
    else:
        y_prob = y_pred
    
    auc_score = roc_auc_score(y_test, y_prob)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='binary')
    prec = precision_score(y_test, y_pred, average='binary')
    
    resultados[nome] = acc
    precisoes[nome] = prec
    f1s[nome] = f1
    roc_aucs[nome] = auc_score
    
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    roc_curves[nome] = (fpr, tpr, thresholds)
    
    print(f"Acurácia: {acc:.4f}")
    print(f"Precisão (binary): {prec:.4f}")
    print(f"F1-score (binary): {f1:.4f}")
    print("Relatório de Classificação:")
    print(classification_report(y_test, y_pred, zero_division=0))

plt.figure(figsize=(8, 6))
for nome, (fpr, tpr, thresholds) in roc_curves.items():
    auc_score = roc_aucs[nome]
    plt.plot(fpr, tpr, label = f"{nome} (AUC = {auc_score:.3f})")
plt.plot([0,1], [0,1])
plt.xlabel("False Positive (FP)")
plt.ylabel("True Positive")
plt.title("Curvas ROC - Comparação entre modelos")
plt.grid(True)
plt.show()

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')  
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate (Fall-Out)', fontsize=14)
    plt.ylabel('True Positive Rate (Recall)', fontsize=14)
    plt.grid(True)

plt.figure(figsize=(10, 7))

for nome, (fpr, tpr, thresholds) in roc_curves.items():
    auc_score = roc_aucs[nome]
    plot_roc_curve(fpr, tpr, label=f"{nome} (AUC = {auc_score:.3f})")

plt.title("Curvas ROC – Comparação Entre Modelos (Formato Estendido)", fontsize=16)
plt.legend(fontsize=12)
plt.show()

print("Gráfico de comparação de acurácia")
plt.figure(figsize=(10,5))
plt.bar(resultados.keys(), resultados.values())
plt.title("Comparação de Acurácia")
plt.ylabel("Acurácia")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

print("Gráfico de precisão")
plt.figure(figsize=(10,5))
plt.bar(precisoes.keys(), precisoes.values(), color='orange')
plt.title("Comparação de Precisão")
plt.ylabel("Precisão")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

print("Gráfico de F1-score")
plt.figure(figsize=(10,5))
plt.bar(f1s.keys(), f1s.values(), color='green')
plt.title("Comparação de F1-score")
plt.ylabel("F1-score")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

print("\nComparação final:")
for nome in resultados:
    print(f"{nome}: Acurácia={resultados[nome]:.4f}, Precisão={precisoes[nome]:.4f}, F1-score={f1s[nome]:.4f}, ROC AUC={roc_aucs[nome]:.4f}")
