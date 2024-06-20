
# Importar as bibliotecas necessárias
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import pandas as pd
import os
import pandas as pd
import json 

## leitura da base
def ler_arquivo(caminho_completo):
    # Verifica se o arquivo existe
    if not os.path.isfile(caminho_completo):
        raise FileNotFoundError(f"O arquivo {caminho_completo} não foi encontrado.")
    
    # Lê o arquivo usando pandas
    df = pd.read_csv(caminho_completo)
    return df

def save_params(model,path):
    model_param = "model.json"
    model_filepath = os.path.join(model_path, model_param)
    with open(model_filepath, 'w') as json_file:
        json.dump(model.get_params(), json_file)


def train_model(wine_data_encoded,model_path):
    # Separar as variáveis independentes (X) da variável dependente (y)
    X = wine_data_encoded.drop(columns=['quality'])
    y = wine_data_encoded['quality']
    
    # Dividir os dados em conjuntos de treino (80%) e teste (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Construir o modelo de Regressão Linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prever no conjunto de teste e avaliar o modelo
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse:.2f}')
    print(f'R^2 Score: {r2:.2f}')

    # Salvar o modelo treinado para uso posterior
    model_filename = 'linear_regression_model.pkl'
    model_filepath = os.path.join(model_path, model_filename)
    
    joblib.dump(model,model_filepath)
    save_params(model,model_path)
    #salvando variaveis
    var_filename = 'vars.json'
    var_filepath = os.path.join(model_path, var_filename)

    # Supondo que X.columns seja uma lista de colunas do DataFrame
    # Convertendo a lista de colunas para JSON e escrevendo no arquivo
    with open(var_filepath, 'w', encoding='utf-8') as file:
        json.dump(list(X.columns), file, ensure_ascii=False, indent=4)
    
    print(f'Modelo salvo como {model_filename}')
    print(f'Parametros salvo scomo {model.get_params()}')

if __name__ == "__main__":
    # setando folder
    dataset_path = os.path.join('red_wine_quality.csv')
    model_path = os.path.join(os.path.dirname(__file__))

    #leitura do arquivo
    caminho_completo = os.path.join(dataset_path)
    dataframe = ler_arquivo(caminho_completo)
    wine_data_encoded = pd.get_dummies(dataframe, columns=['ph'])

    # Treinar o modelo
    train_model(wine_data_encoded,model_path)
