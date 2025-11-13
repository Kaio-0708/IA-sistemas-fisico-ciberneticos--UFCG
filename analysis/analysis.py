import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

file_path = "D:\\IA_UFCG\\heart+disease\\processed.cleveland.data"

columns = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
]

df = pd.read_csv(file_path, sep=",", header=None, names=columns, na_values="?")

print(df.head())
print(df.info())
print(df.describe())

df = df.dropna()
df = df.apply(pd.to_numeric)

print("Após limpeza básica")
print(df.info())
print(df.describe())
print(df['target'].value_counts())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
print("--------")
print("Análise univariada")

sns.set(style="whitegrid")

num_cols = ["age", "trestbps", "chol", "thalach", "oldpeak"]
categoricas_cols = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal", "target"]

print(df[num_cols].describe())
print(df[num_cols].median())

for col in num_cols:
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    sns.histplot(df[col], kde=True, bins=20, color="skyblue")
    plt.title(f"Histograma de {col}")
    plt.subplot(1,2,2)
    sns.boxplot(x=df[col], color="lightgreen")
    plt.title(f"Boxplot de {col}")
    plt.show()
    
    mean = df[col].mean()
    median = df[col].median()
    std = df[col].std()
    print(f"{col}: {mean:.2f}, {median:.2f}, {std:.2f}")
    
for col in categoricas_cols: 
    print(df[col].value_counts())
    
for col in categoricas_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(x= df[col], palette= "pastel")
    plt.title(f"Distribuição de {col}")
    plt.xlabel(col)
    plt.ylabel("Contagem")
    plt.show()

print("-----------")    
print("Análise bivariada / multivariada")

plt.figure(figsize=(12,10))
corr_matrix = df.corr()  
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlação")
plt.show()

strong_corr = corr_matrix.abs().unstack().sort_values(ascending=False)
strong_corr = strong_corr[(strong_corr < 1)]
print("Top 5 correlações fortes:")
print(strong_corr.head(5))

plt.figure(figsize=(6,4))
sns.scatterplot(x="trestbps", y="chol", data=df)
plt.title("Scatter plot: trestbps x chol")
plt.xlabel("Trestbps")
plt.ylabel("Chol")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x="target", y="thalach", data=df, palette="pastel")
plt.title("Boxplot: thalach por target")
plt.xlabel("Target")
plt.ylabel("Thalach")
plt.show()

print(df.isnull().sum())
print(df.duplicated().sum())

print("Detecção de outliers usando Z-score e 1.5*IQR")
outliers = {}
for col in num_cols:
    z_scores = np.abs(stats.zscore(df[col]))
    z_out = df[z_scores > 3]
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    iqr_out = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    print(f"{col}: {len(z_out)} outliers (Z-score), {len(iqr_out)} outliers (IQR)")
    outliers[col] = {"z": z_out, "iqr": iqr_out}

print("Exemplo de transformações: log de oldpeak, dummy para cp")
df['oldpeak_log'] = np.log(df['oldpeak'] + 1)  
df = pd.get_dummies(df, columns=['cp'], prefix='cp')  
df['sex_male'] = df['sex']
df['exang_yes'] = df['exang']

print("Dataset final após análise de dados necessárias conforme aula 06 de EDA e ETL")
print(df.head())
print(df)

df.to_csv("D:\\IA_UFCG\\heart_disease_final.csv", index=False)