"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia'] = {'India': ['Bangalore']}
locations['North America']['USA'].append('Atlanta')
locations['Africa'] = {'Egypt': ['Cairo']}
locations['Asia'].update(China='Shanghai')


def by_value(item):
    return item[1]


def print_cities_countries(dict):
    for country, cities in sorted(dict.items(), key=by_value):
        if isinstance(cities, list):
            for city in cities:
                print("{0} - {1}".format(city, country))
        else:
            print("{0} - {1}".format(cities, country))


print(1)
for city in sorted(locations['North America']['USA']):
    print(city)

print(2)
print_cities_countries(locations['Asia'])


# or


locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print 1
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print city

print 2
asia_cities = []
for countries, cities in locations['Asia'].iteritems():
    city_country = cities[0] + " - " + countries
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print city
