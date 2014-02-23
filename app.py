#!flask/bin/python
from crossdomain_decorator import crossdomain
from flask import Flask, jsonify
from pymongo import MongoClient
import calendar

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.ng_bitcoin_arbitrage

@app.route('/bitcoin-arbitrage/api/v1.0/opportunities', methods = ['GET'])
@crossdomain(origin='*')
def get_opportunities():
    opportunities = list(db.opportunities.find())
    for opportunity in opportunities:
        del opportunity['_id']
        opportunity['updated_on'] = opportunity['updated_on'].strftime('%Y-%m-%dT%H:%M:%SZ') #calendar.timegm(opportunity['updated_on'].utctimetuple()) * 1000

	#db.opportunities.remove()
    return jsonify( { 'opportunities': opportunities } )

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')

