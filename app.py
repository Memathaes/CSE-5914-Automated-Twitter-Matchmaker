from flask import Flask, render_template, url_for, request
import UI

app = Flask(__name__)

# runs using:
# py -m flask --app app run
# or
# python -m flask run


@app.route('/', methods=['POST', 'GET', 'UPDATE'])
def index():
    if request.method == 'POST':
        usr = request.form['content']
        if request.form['submit_button'] == "Find matches":
            tweetList = UI.ui(usr)
            return render_template('matches.html', words=tweetList)
        if request.form['submit_button'] == "Please wait...":
            tweetList = UI.u_click(usr)
            return render_template('update.html', words=tweetList)
        if request.form['submit_button'] == "Update database":
            tweetList = UI.u_click(usr)
            return render_template('update.html', words=tweetList)

    return render_template('index.html')
