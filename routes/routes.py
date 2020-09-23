from __main__ import app
from flask import Response
from service.calculations import BasicStatistic
import logging
import json

logging.basicConfig(level=logging.INFO)


@app.route('/total', methods=['GET'])
def get_total():
    numbers_to_add = list(range(10000001))
    st = BasicStatistic(numbers_to_add)
    total = st.get_total()
    if total == 0:
        return Response('There are no data to summarise ',
                        status=200, mimetype='application/json')
    resp_json = json.dumps({
                'total': total
                })
    return Response(resp_json, status=200, mimetype='application/json')


@app.route('/', methods=['GET'])
def get_default():
    logging.info('Received request for default page')
    info = 'The application has just one endpoint which returns the total. Please call /total.'
    return Response(info, status=200, mimetype='application/json')
