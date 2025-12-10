# Relatório de Classificação Binária

**Visão Geral**

Este projeto implementa e compara o desempenho de diferentes algoritmos de classificação binária em um conjunto de dados supervisionado. Foram avaliados cinco modelos: **Regressão Logística**, **KNN**, **SVM-RBF**, **Random Forest** e **XGBoost**.

## Resultados dos Modelos

### **Regressão Logística**

- **Acurácia:** 0.8778 (87.78%)
- **Precisão (classe 1):** 0.8947
- **F1-score (classe 1):** 0.8608
- **ROC AUC:** 0.9388

### **K-Nearest Neighbors (KNN)**

- **Acurácia:** 0.8778 (87.78%)
- **Precisão (classe 1):** 0.9167
- **F1-score (classe 1):** 0.8571
- **ROC AUC:** 0.9258

### **Support Vector Machine (SVM-RBF)**

**Melhor Modelo**

- **Acurácia:** 0.8889 (88.89%)
- **Precisão (classe 1):** 0.9697
- **F1-score (classe 1):** 0.8649
- **ROC AUC:** 0.9467

### **Random Forest**

- **Acurácia:** 0.8444 (84.44%)
- **Precisão (classe 1):** 0.8462
- **F1-score (classe 1):** 0.8250
- **ROC AUC:** 0.9423

### **XGBoost**

- **Acurácia:** 0.8222 (82.22%)
- **Precisão (classe 1):** 0.8205
- **F1-score (classe 1):** 0.8000
- **ROC AUC:** 0.9009

## Análise Comparativa

### **1. Acurácia**

| Posição | Modelo              | Acurácia |
| ------- | ------------------- | -------- |
| 1º      | SVM-RBF             | 0.8889   |
| 2º      | Regressão Logística | 0.8778   |
| 2º      | KNN                 | 0.8778   |
| 3º      | Random Forest       | 0.8444   |
| 4º      | XGBoost             | 0.8222   |

### **2. Precisão (classe 1)**

| Posição | Modelo              | Precisão |
| ------- | ------------------- | -------- |
| 1º      | SVM-RBF             | 0.9697   |
| 2º      | KNN                 | 0.9167   |
| 3º      | Regressão Logística | 0.8947   |
| 4º      | Random Forest       | 0.8462   |
| 5º      | XGBoost             | 0.8205   |

### **3. F1-score (classe 1)**

| Posição | Modelo              | F1-score |
| ------- | ------------------- | -------- |
| 1º      | SVM-RBF             | 0.8649   |
| 2º      | Regressão Logística | 0.8608   |
| 3º      | KNN                 | 0.8571   |
| 4º      | Random Forest       | 0.8250   |
| 5º      | XGBoost             | 0.8000   |

### **4. ROC AUC**

| Posição | Modelo              | ROC AUC |
| ------- | ------------------- | ------- |
| 1º      | SVM-RBF             | 0.9467  |
| 2º      | Random Forest       | 0.9423  |
| 3º      | Regressão Logística | 0.9388  |
| 4º      | KNN                 | 0.9258  |
| 5º      | XGBoost             | 0.9009  |

## Modelo Vencedor

**SVM-RBF** emergiu como o modelo mais eficiente, alcançando o melhor desempenho em todas as métricas avaliadas:

- Maior acurácia (88.89%)
- Maior precisão para a classe positiva (96.97%)
- Melhor F1-score (86.49%)
- Melhor ROC AUC (94.67%)

## Relatórios de Classificação Detalhados

### **Distribuição das Classes**

- Classe 0: **49** amostras
- Classe 1: **41** amostras

### **Métricas por Modelo**

| Modelo              | Precision C0 | Recall C0 | F1 C0 | Precision C1 | Recall C1 | F1 C1 |
| ------------------- | ------------ | --------- | ----- | ------------ | --------- | ----- |
| Regressão Logística | 0.87         | 0.92      | 0.89  | 0.89         | 0.83      | 0.86  |
| KNN                 | 0.85         | 0.94      | 0.89  | 0.92         | 0.80      | 0.86  |
| SVM-RBF             | 0.84         | 0.98      | 0.91  | 0.97         | 0.78      | 0.86  |
| Random Forest       | 0.84         | 0.88      | 0.86  | 0.85         | 0.80      | 0.82  |
| XGBoost             | 0.82         | 0.86      | 0.84  | 0.82         | 0.78      | 0.80  |

## Conclusão

**SVM-RBF é o modelo mais recomendado para este problema.**
