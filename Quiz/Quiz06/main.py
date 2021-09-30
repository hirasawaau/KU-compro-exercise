# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class City:
  nbCity = 0
  def __init__(s,city,country,lat,long,temp):
    s.city = city; s.country = country; s.lat = lat
    s.long = long; s.temp = temp; City.nbCity += 1
class Country:
  nbCountry = 0
  def __init__(self,country,population,EU,coastline):
    self.country = country
    self.population = population
    self.EU = True if EU == 'yes' else False
    self.coastline = True if coastline == 'yes' else False

def readCity():
  myCity = []
  with open('Cities.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      city,country,lat,long,temp = cc[0],cc[1],float(cc[2]),float(cc[3]),float(cc[4])
      myCity.append(City(city,country,lat,long,temp))
  return myCity

def test_readCity(myCity):
  for c in myCity:
    print(c.city,c.country,c.lat,c.long,c.temp)

def readCountry():
  myCountry = []
  with open('Countries.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      country,population,EU,coastline = cc[0],cc[1],cc[2],cc[3]
      myCountry.append(Country(country,population,EU,coastline))
  return myCountry

def q01(myCity:list, myCountry:list):
  _countrys = [country.country for country in myCountry if country.EU and not country.coastline]
  eu_cities = [c for c in myCity if c.country in _countrys]
  country = {}
  for city in eu_cities:
      try:
          country[city.country].append(city.temp)
      except KeyError:
          country.update({city.country:[city.temp]})
  
  for country,temps in country.items():
      print(country,f'{sum(temps) / len(temps):.2f}')


def q02(myCity, myCountry):
  _countrys = [country.country for country in myCountry if not country.EU]
  # print(_countrys)
  country = {}
  for city in [c for c in myCity if c.country in _countrys]:
      try:
          country[city.country].append(city.temp)
      except KeyError:
          country.update({city.country:[city.temp]})
  
  avgCountry = {}
  for country,temps in country.items():
        avgCountry.update({country:sum(temps) / len(temps)})

  minCountry = min(avgCountry,key=lambda country:avgCountry[country])
  maxCountry = max(avgCountry,key=lambda country:avgCountry[country])

  print(f'The highest average city temperature: {maxCountry} ({avgCountry[maxCountry]:.2f})')
  print(f'The lowest average city temperature: {minCountry} ({avgCountry[minCountry]:.2f})')


### main begins here
myCity = readCity()
myCountry = readCountry()


# %%
q01(myCity,myCountry)


# %%
q02(myCity,myCountry)


