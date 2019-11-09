import re

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

flag = "{fctf_valhalla}"
pattern_ua = re.compile(r'(^|\b)neptune($|\b)', re.I)
pattern_referrer = re.compile(r'(^|\b)boris($|\b)', re.I)

@app.route('/')
def home():
    is_good_ua = re.match(pattern_ua, request.user_agent.string or '') is not None
    is_good_referrer = re.match(pattern_referrer, request.referrer or '') is not None

    if not is_good_ua:
        return "Hey.. use special browser only!"
    elif not is_good_referrer:
        return "Wait.. http said you are not from Boris? Go away!"
    else:
        return flag
