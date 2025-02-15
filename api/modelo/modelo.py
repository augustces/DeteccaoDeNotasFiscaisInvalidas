from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
import pandas as pd
import logging
import joblib
import os

# Configuração do logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_data(filepath):
    """Carrega os dados a partir de um arquivo CSV, garantindo que ele existe."""
    if not os.path.exists(filepath):
        logging.error(f"Arquivo {filepath} não encontrado!")
        raise FileNotFoundError(f"Arquivo {filepath} não encontrado!")

    df = pd.read_csv(filepath, delimiter=";")
    logging.info("Dados carregados com sucesso.")
    return df

def preprocess_data(df):
    """Realiza pré-processamento dos dados."""
    logging.info("Iniciando pré-processamento de dados...")
    
    # Remoção de valores nulos em colunas críticas
    df = df.dropna(subset=["id_supplier"])
    
    # Engenharia de features
    df = df.drop(['id', 'calculated_value', 'inss_tax_rate', 'issue_date', 'lc116', 'state'], axis = 1)
    
    # Conversão de variáveis booleanas para inteiros
    bool_cols = df.select_dtypes(include=["bool"]).columns
    df[bool_cols] = df[bool_cols].astype(int)
    
    # Codificação da variável target
    df["class_label"] = df["class_label"].map({"not valid": 0, "valid": 1})

    logging.info("Pré-processamento concluído.")
    return df

def split_data(df):
    """Divide o conjunto de dados em treino e teste."""
    X = df.drop('class_label', axis=1)
    y = df['class_label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, shuffle=True)
    
    logging.info(f"Divisão dos dados: {X_train.shape[0]} amostras para treino e {X_test.shape[0]} amostras para teste.")
    return X_train, X_test, y_train, y_test

def balance_data(X_train, y_train):
    """Aplica SMOTE para balancear o conjunto de treino."""
    logging.info("Aplicando SMOTE para balanceamento de dados...")
    
    sm = SMOTE(random_state=42)
    X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

    logging.info(f"Após SMOTE: {X_train_res.shape[0]} amostras balanceadas.")
    return X_train_res, y_train_res

def train_model(X_train, y_train):
    """Treina o modelo RandomForest."""
    logging.info("Iniciando treinamento do modelo RandomForest...")

    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)

    logging.info("Treinamento concluído.")
    return rf

def evaluate_model(model, X_test, y_test):
    """Avalia o modelo treinado e mostra as métricas no terminal"""
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_proba)

    logging.info("Avaliação concluída.")
    logging.info(f'Accuracy       :{round(acc, 3)}')
    logging.info(f'Precision      :{round(prec, 3)}')
    logging.info(f"Recall         :{round(rec, 3)}", )
    logging.info(f"F1 Score       :{round(f1, 3)}", )
    logging.info(f"ROC AUC        :{round(roc_auc, 3)}" )

def save_model(model, filename="random_forest_model.pkl"):
    """Salva o modelo treinado na pasta 'modelo' dentro do projeto."""

    # Garante que a pasta "modelo" exista
    model_dir = os.path.join(os.getcwd(), "modelo")
    os.makedirs(model_dir, exist_ok=True)  # Cria a pasta se ela não existir
    
    # Define o caminho completo do arquivo
    model_path = os.path.join(model_dir, filename)
    
    # Salva o modelo
    joblib.dump(model, model_path)
    logging.info(f"Modelo salvo em {model_path}")

# Pipeline principal
def main(filepath):
    df = load_data(filepath)
    df = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(df)
    X_train_res, y_train_res = balance_data(X_train, y_train)
    model = train_model(X_train_res, y_train_res)
    evaluate_model(model, X_test, y_test)
    save_model(model)

# Executa o pipeline com um arquivo CSV de entrada
if __name__ == "__main__":
    main('../dataset/notasfiscais.csv')
