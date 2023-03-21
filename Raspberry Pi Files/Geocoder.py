try:
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="smyGeocoder")
    address, (latitude, longitude) = geolocator.geocode(input('Enter the name: '))
    print(address, latitude, longitude)
    location = geolocator.reverse(input('Enter the co-ordinates: '))
    print(location)
except:
    print('error')
finally:    
    input('\nPress ENTER to exit')
