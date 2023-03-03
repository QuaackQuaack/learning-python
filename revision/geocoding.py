import urllib.parse, urllib.request, urllib.error
import json
import ssl

api_key = False

if api_key == False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#to ignore ssl certified error

cntxt = ssl.create_default_context()
cntxt.check_hostname = False
cntxt.verify_mode = ssl.CERT_NONE

while True:
    address = input('enter  a adress you want ')
    if len(address) < 1 : break

    parameters = dict()
    parameters['address'] = address
    
    if api_key is not False: parameters['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parameters) # here url is in correct form 
    print('retrieving ' , url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieving',len(data),'character')

    try :
        js = json.loads(data) # it converts valid json string into python  dictionary

    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK' :
        print('========failure=========')
        print(data)
        continue

    print(json.dumps(js, indent= 4)) # dumps convert python object into json string

    lat = js['results'][0]['geometry']['location']['lat']
    long = js['results'][0]['geometry']['location']['lng']

    print('lat ' , lat , 'long' , long)
    location = js['results'][0]['formatted_address']
    print(location)

    








