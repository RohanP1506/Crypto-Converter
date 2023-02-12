# Crypto Converter

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