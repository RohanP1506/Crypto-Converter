from pycoingecko import CoinGeckoAPI
import datetime
import time

cg = CoinGeckoAPI()


#list of ALL formatted dates, use for GRAPH
def getFormattedDates(datelist):
  formatted_list = []
  for unix in datelist:
    timestamp = datetime.datetime.fromtimestamp(unix)
    dateUS = timestamp.strftime('%m-%d-%Y')
    formatted_list.append(dateUS)
  return formatted_list


#per date format, used to correctly call data
def formatDate(date):
  timestamp = datetime.datetime.fromtimestamp(date)
  dateUS = timestamp.strftime('%m-%d-%Y')
  return dateUS


#dates for unix conv, call data
def getListDates(limit):
  year = datetime.date.today().year - int(limit)
  datelist = []
  for num in range(1, int(limit) + 1):
    month = 1
    for num in range(1, 13):
      date = datetime.date(year, num, 1)
      year = int(date.year)
      month = int(date.month)
      day = int(date.day)
      datelist.append(str(month) + '-' + str(day) + '-' + str(year))
      month += 1
    year += 1
  return datelist


#unix codes, call data
def getUNIXDates(datelist):
  unix_list = []
  for date in datelist:
    oneDate = datetime.datetime.strptime(date, '%m-%d-%Y')
    unix = time.mktime(oneDate.timetuple())
    unix_list.append(int(unix))
  return unix_list


# coin data
def getCoinData(coin, years):
  count = 0
  finalList = {}
  unix_list = getUNIXDates(getListDates(years))
  coinJson = cg.get_coin_market_chart_range_by_id(
    id=coin,
    vs_currency='usd',
    from_timestamp=str(unix_list[0]),
    to_timestamp=str(unix_list[-1]))
  path = coinJson['prices']
  for list, date in zip(path, unix_list):
    formatted = formatDate(date)
    finalList[formatted] = "%.4f" % list[1]
    count += 1
  return finalList


# full dict
def combine(coin1, coin2, year):
  json1, json2 = getCoinData(coin1, year), getCoinData(coin2, year)
  output = {}
  for key in json1.keys():
    output[key] = [json1[key], json2[key]]
  return output


# Name and ids
def convertCoin(id):
  coins = cg.get_coins_list()
  for coin in coins:
    if coin['name'] == id:
      return coin['id']
  return -1


def getSupportedCoins():
  supportedlist = []
  x = cg.get_coins_list()
  for name in x:
    supportedlist.append(name['name'])
  return supportedlist
