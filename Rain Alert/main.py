import requests
from twilio.rest import Client
api_key = "c05b55f85fd87896c813c8d892108c3b"
OWN_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
acc_sid = 'ACad73f2d04e15642ad65e03c055c4959e'
auth_token = 'f0264bff43ca10cb93dbf8fd416de9f0'

LAT = 47.158455
LONG = 27.601442
parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': api_key
}
response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
current_weather = weather_data['weather'][0]['id']
print(current_weather)

if int(current_weather) > 700:
    client = Client(acc_sid, auth_token)
    message = client.messages \
        .create(
        body="Cf Vanesa, am facut un program care trimite sms, sunt bun csf, dar raspunde si tu la mesaje pe mess pup pa.",
        from_='+15676666916',
        to='+40 744 866 918'
    )
    print(message.status)

