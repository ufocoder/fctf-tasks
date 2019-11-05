from flask import Flask, request, jsonify, render_template
from morse import encode_text, decode_text

app = Flask(__name__)

text_error = 'enter help for all commands'
text_author = 'there are not the droids you are looking for'
text_help = 'help - the current command. key - key for next task. author - author of the task.'

text_key = "{fctf_mmmmmooorrssse}"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    try:
        decodedText = decode_text(request.json['cmd'])
    except:
        decodedText = ''

    if decodedText == 'help':
        return encode_text(text_help)

    if decodedText == 'key':
        return text_key

    if decodedText == 'author':
        return encode_text(text_author)

    return encode_text(text_error)
