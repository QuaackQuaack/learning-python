import re
txt = 'yesma chai iamconorscafer@gmail.com find garni ho @2pm'
result = re.findall('\S+@\S+',txt)
print(result)
