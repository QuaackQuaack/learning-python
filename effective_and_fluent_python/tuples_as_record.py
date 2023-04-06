
lax_coordinats = (33.9374, -212.474)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP','XDA204856')] # this can be tuple bound with list

for passport  in sorted(traveler_ids):
    print('%s/%s' %passport) # like in C we can also do in python damnnnnnnnnnnnnnnnnnnn

#for normal mode 
for country, number in sorted(traveler_ids):
    print(f'{country}/{number}')

for country,_ in traveler_ids: # _ is called dummy variable 
    print(country)




