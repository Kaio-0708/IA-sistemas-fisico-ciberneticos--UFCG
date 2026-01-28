### Informações Gerais do Dataset

| Atributo | Total de Entradas | Tipo  | Valores Ausentes |
| -------- | ----------------- | ----- | ---------------- |
| age      | 303               | float | 0                |
| sex      | 303               | float | 0                |
| cp       | 303               | float | 0                |
| trestbps | 303               | float | 0                |
| chol     | 303               | float | 0                |
| fbs      | 303               | float | 0                |
| restecg  | 303               | float | 0                |
| thalach  | 303               | float | 0                |
| exang    | 303               | float | 0                |
| oldpeak  | 303               | float | 0                |
| slope    | 303               | float | 0                |
| ca       | 299               | float | 4                |
| thal     | 301               | float | 2                |
| target   | 303               | int   | 0                |

Após limpeza de valores ausentes, o dataset final contém **297 amostras e 14 atributos**.

---

### Estatísticas Descritivas (Após Limpeza)

| Variável                                 | Média  | Mediana | Desvio Padrão | Mínimo | Máximo |
| ---------------------------------------- | ------ | ------- | ------------- | ------ | ------ |
| **Idade (age)**                          | 54.54  | 56.0    | 9.05          | 29     | 77     |
| **Pressão de repouso (trestbps)**        | 131.69 | 130.0   | 17.76         | 94     | 200    |
| **Colesterol (chol)**                    | 247.35 | 243.0   | 52.00         | 126    | 564    |
| **Frequência cardíaca máxima (thalach)** | 149.60 | 153.0   | 22.94         | 71     | 202    |
| **Depressão ST (oldpeak)**               | 1.06   | 0.8     | 1.17          | 0.0    | 6.2    |

---

### Distribuição das Variáveis Categóricas

| Variável                                  | Categorias Principais                     | Contagem |
| ----------------------------------------- | ----------------------------------------- | -------- |
| **Sexo (sex)**                            | 1.0 (masculino): 201 • 0.0 (feminino): 96 |
| **Tipo de dor no peito (cp)**             | 4.0: 142 • 3.0: 83 • 2.0: 49 • 1.0: 23    |
| **Glicemia > 120 mg/dl (fbs)**            | 1.0: 43 • 0.0: 254                        |
| **Eletrocardiograma (restecg)**           | 0.0: 147 • 2.0: 146 • 1.0: 4              |
| **Angina induzida por exercício (exang)** | 0.0: 200 • 1.0: 97                        |
| **Inclinação do segmento ST (slope)**     | 1.0: 139 • 2.0: 137 • 3.0: 21             |
| **Vasos principais coloridos (ca)**       | 0.0: 174 • 1.0: 65 • 2.0: 38 • 3.0: 20    |
| **Talassemia (thal)**                     | 3.0: 164 • 7.0: 115 • 6.0: 18             |
| **Classe-alvo (target)**                  | 0: 160 • 1: 54 • 2: 35 • 3: 35 • 4: 13    |

---

### Correlações Mais Fortes

| Par de Variáveis    | Correlação |
| ------------------- | ---------- |
| `slope` ↔ `oldpeak` | **0.579**  |
| `ca` ↔ `target`     | **0.521**  |
| `thal` ↔ `target`   | **0.513**  |

Essas correlações sugerem:

- **Maior número de vasos coloridos (`ca`)** e **tipo de talassemia (`thal`)** se associam a maior probabilidade de doença cardíaca.
- A variável **oldpeak** (depressão ST) tem forte relação com a **inclinação do segmento ST (`slope`)**, o que é clinicamente coerente.

---

### Detecção de Outliers

| Variável   | Outliers (Z-score) | Outliers (IQR) |
| ---------- | ------------------ | -------------- |
| `age`      | 0                  | 0              |
| `trestbps` | 2                  | 9              |
| `chol`     | 4                  | 5              |
| `thalach`  | 1                  | 1              |
| `oldpeak`  | 2                  | 5              |

---

### Transformações Aplicadas

- **Log-transform**: `oldpeak_log = log(oldpeak + 1)`
- **One-hot encoding**: variável `cp` expandida para `cp_1.0`, `cp_2.0`, `cp_3.0`, `cp_4.0`
- **Variáveis binárias derivadas**:
  - `sex_male` (1 se masculino)
  - `exang_yes` (1 se possui angina induzida por exercício)

O dataset final resultou em **20 colunas** após todas as transformações.

---

## A análise exploratória revelou padrões importantes:

- A média de idade é **54,5 anos**, com predominância de **homens (68%)**.
- As principais variáveis correlacionadas à doença cardíaca são **ca**, **thal** e **oldpeak**.
- O dataset é bem estruturado e apresenta **baixa presença de outliers**.
- Após a limpeza e codificação, o conjunto de dados está **pronto para modelagem preditiva**.

---

### Tamanho Final do Dataset

**297 amostras × 20 variáveis**
