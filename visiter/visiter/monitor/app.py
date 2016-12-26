# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 2016/12/25 15:00
'''
import json
from flask import Flask, render_template, jsonify, request, current_app
import redis
from settings import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', timeinterval=TIMEINTERVAL, stats_keys=STATS_KEYS)


@app.route('/ajax')
def ajax():
    key = request.args.get('key')
    result = current_app.r.lrange(key, -POINTLENGTH, -1)[::POINTINTERVAL]
    if not current_app.spider_is_run:
        # spider is closed
        return json.dumps(result).replace('"', ''), 404
    return json.dumps(result).replace('"', '')


@app.route('/signal')
def signal():
    signal = request.args.get('sign')
    if signal == 'closed':
        current_app.spider_is_run = False
    elif signal == 'running':
        current_app.spider_is_run = True
    return jsonify('')


@app.before_first_request
def init():
    current_app.r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    current_app.spider_is_run = True if current_app.r.get('spider_is_run') == '1' else False


if __name__ == '__main__':
    app.run(debug=False, host=APP_HOST, port=APP_PORT)
