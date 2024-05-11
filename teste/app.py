import requests
from flask import Flask, render_template


app = Flask(__name__)




def get_weather_data(city):
    chave_api = 'sua_chave_api_aqui'
    url_base = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid':chave_api, 'units': 'metrics','lang':'pt_br'}

    response = requests.get(url_base, params=params)

    if response.status_code ==200:
        wheather_data = response.json()
        return wheather_data
    else:
        print("Erro ao obter dados meteorologicos", response.status_code)


city_name = 'porto velho'
weather_data = get_weather_data(city_name)

if get_weather_data:
    print("Funcionou oh, os dados sao os seguintes:", city_name,":")
    print(weather_data)
    

else: 
    print("falhou carai hiihi")


@app.route("/")
def buscar():
    return get_weather_data('city')



if __name__ == '__main__':
     app.run(debug=True)