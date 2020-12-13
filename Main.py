
import os
import yfinance as yf
from flask import Flask, request

app = Flask(__name__)

@app.route('/getdata', methods=['GET'])
def respond():
  try:
    TICKER = request.args.get('ticker')
    return yf.Ticker(str(TICKER)).info
  except:
    return {}

@app.route('/', methods=['GET'])
def rooturl():
  return '.'
  
if __name__ == '__main__':
  port = int(os.environ.get("PORT", 33333))
  app.run(threaded=True, host='0.0.0.0', port=port)
