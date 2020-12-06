pages = 4

loc_code = ['STATION%5E1442']

max_index = (24 * pages) - 24

index = [i for i in range(0, max_index, 24)]

radius = [0.0, 0.25, 0.5, 1.0, 3.0, 5.0, 10.0, 15.0, 20.0, 30.0, 40.0]

prop_type = ['detached', 'semi-detached', 'terraced', 'flat', 'bungalow', 'land', 'park-home']

url_part_1 = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier='

url_part_2 = '&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords='