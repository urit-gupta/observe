import sys
from datetime import date, time
from calc.utils import location

def user_parameters():
  # country -> 38 is Canada
  cities = location.read_cities()
  countries = list(cities.keys())
  countries.sort()
  sys.stdout.write('Choose country by index: [Enter the index number as displayed and hit the RETURN/ENTER key]' + '\n')
  for i in range(len(countries)):
    sys.stdout.write(str(i + 1) + '. ' + countries[i] + '\n')
  country_index = int(sys.stdin.readline().strip())
  cities_in_country = cities[countries[country_index - 1]]
  cities_in_country.sort(key=lambda e: e[0])
  city_names = list(map(lambda e: e[0], cities_in_country))

  # city -> 72 in Canada is Charlottetown
  sys.stdout.write('Choose city by index: [Enter the index number as displayed and hit the RETURN/ENTER key]' + '\n')
  for i in range(len(city_names)):
    sys.stdout.write(str(i + 1) + '. ' + city_names[i] + '\n')
  city_index = int(sys.stdin.readline().strip())
  city = cities_in_country[city_index - 1]
  sys.stdout.write('You chose the city of ' + city[0] + '.' + '\n')

  # time range
  sys.stdout.write('Choose local time for start of viewing window: [hh:mm in 24h time]' + '\n')
  start_time = sys.stdin.readline().strip().split(':')
  start_time = time(int(start_time[0]), start_time[1], 0)
  sys.stdout.write('Choose local time for end of viewing window: [hh:mm in 24h time]' + '\n')
  end_time = sys.stdin.readline().strip().split(':')
  end_time = time(int(end_time[0]), end_time[1], 0)

  # objects of interest
  # telescope minimum latitude
  # days
