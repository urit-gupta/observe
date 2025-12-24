import pandas

def read_cities():
  cities_data = pandas.read_csv('calc/data/worldcities.csv')
  cities = {}
  for i in range(1, cities_data.shape[0]):
    key = cities_data.iat[i, 4] + ' (' + cities_data.iat[i, 6] + ')'
    if key not in cities:
      cities[key] = []
    cities[key].append((cities_data.iat[i, 1], cities_data.iat[i, 2], cities_data.iat[i, 3]))
  return cities
