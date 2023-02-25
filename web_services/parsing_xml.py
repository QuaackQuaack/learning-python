import xml.etree.ElementTree as ET # for parsing XML 
#In xml doc chai divide as top element(person) and tags(name)
data = '''
<person>
    <name>Chuck</name>
    <phone type='intl'>
    +45555555555
    </phone>
    <email hide='yes'/>
</person> '''

tree = ET.fromstring(data) #from converts string representation of XML intro 'tree'
print(tree)
print('Name:', tree.find('name').text)
print(tree.find('email').text)
print('Attr:',tree.find('email').get('hide'))

