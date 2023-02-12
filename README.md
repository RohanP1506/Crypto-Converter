# Crypto Comparer
Crypto Comparer is a website created with Flask to compare the prices of two cryptocurrencies. 

Documentations:<br>
 - [Chart.js](https://www.chartjs.org/)
 - [Date to UNIX timestamp](https://www.tutorialspoint.com/How-to-convert-Python-date-to-Unix-timestamp)
 - [CoinGecko API](https://www.coingecko.com/en/api/documentation)
 - [pycoingecko](https://github.com/man-c/pycoingecko)

Old json data parse function:
```py
def getCoinData(coin, third):
  years = int(third)
  newCoin = coin.lower()
  datelist = getListDates(2023 - years, years)
  newDictionary = {}
  for date in datelist:
    coinJson = cg.get_coin_history_by_id(id=newCoin, date=str(date),localization='en') 
    newDictionary[date] = coinJson['market_data']['current_price']['usd']
  return newDictionary
```

Old day-month-year list generator:
```py
def getListDates(year, limit):
  datelist = []
  for num in range(1, limit + 1):
    month = 1
    for num in range(1, 13):
      date = datetime.date(year, num, 1)
      year = int(date.year)
      month = int(date.month)
      day = int(date.day)
      datelist.append(str(day) + '-' + str(month) + '-' + str(year))
      month += 1
    year += 1
  return datelist
```


This prints all the names ofsupported crypto coins in html form
```py
def getSupportedCoins():
  file = open('file.txt', 'w')
  hi = []
  x = cg.get_coins_list()
  for shit in x:
    file.wr("<option>" + shit['name'] + "</option>\n")
```

I forgot what this function did but it looks cool
```py
def getSupportedCoins():
  # file = open('file.txt', 'w')
  x = cg.get_coins_list()
  for shit in x:
    print(shit['id'])
```

This function does a thing that happens to do a thing that uses 3 things to do a thing that doesn't even print the correct thing, and has wasted many things (braincells and time)
```py
def getPercentGrowth(coin1, coin2, years):
  coinOneGrowths = []
  coinTwoGrowths = []
  json1, json2 = (getCoinData(coin1, years)), (getCoinData(coin2, years))
  pricelist1 = list(json1.values())
  for count in range(1, len(list(json1.values()))):
    subtracting = float(pricelist1[count]) - float(pricelist1[count - 1])
    dividing = subtracting / float(pricelist1[count - 1])
    finalthing = abs(dividing * 100)
    coinOneGrowths.append(finalthing)
    print(finalthing)

  for count in range(1, len(list(json2.values()))):
    growthcalc2 = abs(((float(list(json2.values())[count]) - float(list(json2.values())[count - 1]) / float(list(json2.values())[count - 1])) * 100))
    coinTwoGrowths.append(growthcalc2)
  growths = {}
  firstkey = list(json1.keys())[0]
  growths[firstkey] = [0, 0]
  for key in getCoinData(coin1, years).keys():
    for growth1, growth2 in zip(coinOneGrowths, coinTwoGrowths):
      growths[key] = [growth1, growth2]
  return growths

print(getPercentGrowth("bitcoin", "dogecoin", "2"))
```