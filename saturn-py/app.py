from flask import Flask, request, render_template, make_response, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('flag', '_together}')
    return resp

@app.route('/xhr', methods=['GET', 'POST'])
def xhr():
    if request.method == 'POST':
        return r"_flock"
    return ""

@app.route('/logo192.png')
@app.route('/robots.txt')
@app.route('/manifest.json')
@app.route('/script.js')
def static_from_root():
    print(app.static_folder, request.path[1:])
    return send_from_directory(app.static_folder, request.path[1:])
