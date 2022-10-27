from flask import Flask, render_template, url_for, request
import UI

app = Flask(__name__)

# runs using:
# py -m flask --app hello run


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        usr = request.form['content']
        tweetList = UI.ui(usr)
        longstring = ""
        for text in tweetList:
            longstring += text + "<br/>"
        return "<p>" + longstring + "</p>"
    else:
        return render_template('index.html')
