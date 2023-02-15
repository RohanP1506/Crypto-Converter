from concurrent.futures import ThreadPoolExecutor
from flask import Flask, render_template, request
from functions import *

app = Flask('Crypto Converter',
            static_folder='static',
            template_folder="templates")


@app.route('/', methods=["GET", "POST"])
def home():
  homedata = {'supportedcoins': getSupportedCoins()}
  return render_template('index.html', data=homedata)


@app.route('/results', methods=["GET", "POST"])
def GraphGenerator():
  coin1 = str(request.form.get('first'))
  coin2 = str(request.form.get('second'))
  years = request.form.get('third')
  dates = []
  firstmoney = []
  secondmoney = []
  for keys, values in getCoinData(convertCoin(coin1), years).items():
    dates.append(keys)
    firstmoney.append(values)
  for keys, values in getCoinData(convertCoin(coin2), years).items():
    secondmoney.append(values)

  graphdata = {
    'firstmoney': firstmoney,
    'dates': dates,
    'secondmoney': secondmoney,
    'coin1': coin1,
    'coin2': coin2,
    'combined': combine(convertCoin(coin1), convertCoin(coin2), years)
  }
                        
  return render_template('results.html', data=graphdata)


@app.route('/about', methods=['GET', 'POST'])
def about():
  return render_template("about.html")


app.run(host='0.0.0.0', port=6969)
