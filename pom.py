str = 'X-DSPAM-Confidence:0.8475'
front = str.find('0')
back = str.find('5')
result=str[front:back+1]
print(result)


