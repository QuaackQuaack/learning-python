# this program is to compare listcomp and map/filter
# lambda can we used in list comprehension 

symbols = '$¢£¥€¤'
ordinal_value = [ ord(s) for s in symbols if ord(s) > 127 ]
print(ordinal_value) #this is from listcomp

#from map way 
map_way = list(filter(lambda c : c > 127 , map(ord, symbols)))
print(map_way)

