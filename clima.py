import requests
import pandas as pd
from datetime import datetime

# Sua API Key do OpenWeather (substitua 'YOUR_API_KEY' pela chave real)
API_KEY = '20841afe111bed2a4345c0ac5d1d0584'
CITY = 'São Paulo,BR'  # Cidade que você quer consultar

# URL da API OpenWeather (usando o endpoint "current weather")
url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# Fazendo a requisição
response = requests.get(url)
data = response.json()

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extrair dados relevantes
    temperature = data['main']['temp']  # Temperatura em Celsius
    humidity = data['main']['humidity']  # Umidade em %
    description = data['weather'][0]['description']  # Descrição do tempo
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Data e hora

    # Criar um dicionário com os dados
    weather_data = {
        'Cidade': [CITY],
        'Temperatura (°C)': [temperature],
        'Umidade (%)': [humidity],
        'Descrição': [description],
        'Data/Hora': [timestamp]
    }

    # Converter para DataFrame com pandas
    df = pd.DataFrame(weather_data)

    # Salvar em CSV
    df.to_csv('clima_sao_paulo.csv', index=False)
    print("Dados salvos em 'clima_sao_paulo.csv'")
    print(df)
else:
    print(f"Erro na requisição: {response.status_code}")