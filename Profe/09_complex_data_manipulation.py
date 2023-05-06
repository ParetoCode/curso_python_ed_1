response_gps = {'country': 'es', 'city': 'Jaen', 'ip':10000}



def gps_get_localition():
    request_ip = response_gps.pop('ip')
    return response_gps , request_ip

location, ip = gps_get_localition()

assert location == {'country': 'es', 'city': 'Jaen'}

def weather_api(country, city):
    assert country == 'ES'
    assert city == 'JAEN'
    return 'rainy', 'sunny'

def parse_data(location):
    country = location.get('country')
    country = country.upper()

    city = location.get('city')
    city = city.upper()

    return country, city

country, city = parse_data(location)
today_prevision, tomorrow_prevision = weather_api(country, city)

assert weather_api(country, city) == (today_prevision, tomorrow_prevision)



