#JSON is build by dictionaries and lists 
#We use built-in library to parse the JSON

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data) #to parse json 
print('User count:',len(info))

for item in info:
    print("Nane ",item['name'])
    print('Id ', item['id'])
    print('Attribute',item['x'])


