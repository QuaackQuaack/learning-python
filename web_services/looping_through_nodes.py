import xml.etree.ElementTree as ET
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input) # convert string representation to xml tree
lst = stuff.findall('users/user') # findall retrives all subtrees in XML tree
#we need to include all parent lvl element in findall 
#otherwise python will not find any desired nodes
print('user count:',len(lst))

for item in lst:
    print('Name',item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute', item.get('x'))
                
        
