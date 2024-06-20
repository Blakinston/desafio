from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Inicializar o Flask
app = Flask(__name__)

# Tentar carregar o modelo
try:
    model = joblib.load('linear_regression_model.pkl')
    print("Modelo carregado com sucesso")
except Exception as e:
    model = None
    print(f"Erro ao carregar o modelo: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Modelo não carregado'}), 500

    try:
        # Obter os dados do request
        data = request.get_json(force=True)
        print(f"Dados recebidos: {data}")

        # Converter para DataFrame
        data_df = pd.DataFrame([data])
        print(f"Dados convertidos para DataFrame: {data_df}")

        # Renomear as colunas conforme necessário
        column_mapping = {
            'pH': 'ph_acid',
            'quality': 'ph_basic'
        }
        data_df = data_df.rename(columns=column_mapping)
        print(f"Dados com colunas renomeadas: {data_df}")

        # Fazer a previsão
        prediction = model.predict(data_df)
        print(f"Previsão: {prediction}")

        # Retornar a previsão
        return jsonify({'prediction': prediction[0]})
    
    except Exception as e:
        # Imprimir o erro detalhado no console
        print(f"Erro ao processar a solicitação: {e}")
        return jsonify({'error': f"Erro interno no servidor: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
