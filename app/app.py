import streamlit as st 
import pandas as pd 
import joblib
import numpy as np
import os

"""
model = joblib.load("../models/svm_rbf_model.pkl")
scaler = joblib.load("../models/scaler.pkl")
features = joblib.load("../models/features.pkl")
"""
current_dir = os.getcwd()
model_path = os.path.join(current_dir, "models", "svm_rbf_model.pkl")
scaler_path = os.path.join(current_dir, "models", "scaler.pkl")
features_path = os.path.join(current_dir, "models", "features.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
features = joblib.load(features_path)

st.set_page_config(page_title="IA - Doença Cardíaca", layout="centered")

st.title("Sistema de Predição de Doença Cardíaca com IA")
st.write("Preencha os dados clínicos do paciente:")

age = st.number_input("Idade", 1, 120, 50)
sex = st.selectbox("Sexo", [0, 1], format_func=lambda x: "Feminino" if x == 0 else "Masculino")
cp = st.selectbox("Tipo de dor no peito (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Pressão arterial em repouso", 80, 250, 120)
chol = st.number_input("Colesterol", 100, 600, 200)
fbs = st.selectbox("Glicemia > 120 mg/dl", [0, 1])
restecg = st.selectbox("ECG em repouso", [0, 1, 2])
thalach = st.number_input("Frequência cardíaca máxima", 60, 220, 150)
exang = st.selectbox("Angina induzida por exercício", [0, 1])
oldpeak = st.number_input("Oldpeak (depressão ST no eletrocardiograma (ECG))", 0.0, 6.0, 1.0)
slope = st.selectbox("Inclinação do ST", [0, 1, 2])
ca = st.selectbox("Número de vasos coloridos (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thal", [1, 2, 3])

if st.button("Avaliar risco conforme"):
    input_data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal,
        "sex_male": sex,
        "exang_yes": exang
    }
    
    input_df = pd.DataFrame([input_data])
    input_df["oldpeak_log"] = np.log(input_df["oldpeak"] + 1)
    
    for i in range(4):
        input_df[f"cp_{i}"] = 1 if cp == i else 0
    
    for col in features:
        if col not in input_df.columns:
            input_df[col] = 0
            
    input_df = input_df[features]
    
    input_scaled = scaler.transform(input_df)
    
    probability = model.predict_proba(input_scaled)[0][1]
    pred = model.predict(input_scaled)[0]
    
    if pred == 1:
        st.error(f" Alto risco de doença cardíaca\n\nProbabilidade: {probability:.2%}")
        st.error(""" **Recomendações:**
        - Consulte um cardiologista o quanto antes
        - Realize exames complementares
        - Monitore sinais como dor no peito e falta de ar
        - Mantenha acompanhamento médico regular""")
    else:
        st.success(f" Baixo risco de doença cardíaca\n\nProbabilidade: {probability:.2%}")
        st.success("""
        **Recomendações:**
        - Mantenha hábitos saudáveis
        - Continue com check-ups regulares
        - Pratique exercícios físicos
        - Alimentação balanceada
        """)
    
