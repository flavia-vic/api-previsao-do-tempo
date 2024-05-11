from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask import send_from_directory
import requests
import datetime
from datetime import datetime


app = Flask(__name__,  static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'db4c1a2efa5032836aeb931226ceacae'  

class WeatherForm(FlaskForm):
    city = StringField('Cidade')
    submit = SubmitField('Obter Tempo')

#Função para converter sunset e sunrise em horas
def converter_horas(timestamp):
  timestamp_seconds = int(timestamp)
  time_obj = datetime.fromtimestamp(timestamp_seconds)
  return time_obj.strftime("%H:%M")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = WeatherForm()

    if form.validate_on_submit():
        city_name = form.city.data
        weather_data = get_weather_data(city_name)

        if 'temperature' in weather_data:
            weather_data['sunrise_hours'] = converter_horas(weather_data['sunrise'])
            weather_data['sunset_hours'] = converter_horas(weather_data['sunset'])

            return render_template('result.html', weather_data=weather_data, city=city_name)
        else:
            
            flash("Por favor, insira um nome de cidade válido.", 'error')

    return render_template('form.html', form=form)


def get_weather_data(city):
    api_key = 'db4c1a2efa5032836aeb931226ceacae'  
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {'q': city, 'appid': api_key, 'lang':'pt_br', 'units':'metric'}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temp = int(weather_data['main']['temp'])
        desc = weather_data['weather'][0]['description']
        wind = int(round(weather_data['wind']['speed'] * 3.6))
        temp_min= int (weather_data['main']['temp_min'] )
        temp_max= int(weather_data['main']['temp_max'])
        deg = (weather_data['wind']['deg']) 
        country = (weather_data['sys']['country'])
        sunrise = int(weather_data['sys']['sunrise'])
        sunset = int(weather_data['sys']['sunset'])
        lon = (weather_data['coord']['lon'])
        lat = (weather_data['coord']['lat'])
        


        weather_data['description'] = desc


        return {'temperature': temp, 'description': desc, 'wind_speed': wind, 'temp_min': temp_min, 'temp_max':temp_max,'deg':deg ,'country':country, 'sunrise':sunrise,'sunset':sunset, 'lon':lon, 'lat':lat}
    
    return {}  



if __name__ == '__main__':
    app.run(debug=True)
    app.config['FLASH_MESSAGES'] = True
