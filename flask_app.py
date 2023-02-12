
#!python 3.6

from flask import render_template, redirect
from flask import Flask
from flask import request
import web_parse

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def jahTime():
    userName = ''
    userAge = ''
    jahAge = ''
    if request.method == 'POST' and 'userAge' in request.form:
        userName = request.form.get('userName')
        userAge = request.form.get('userAge')
        jahAge = str(round(((float(int(userAge) / 0.69444444444444)) / 60) - 0.5)) + str(' hours and ') + str(
            round(float(int(userAge) / .69444444444444) % 60)) + str(' minutes')  # the - 0.5 is to force rounding down
        # jahAgeDays =
        # jahAgeHrs =
    return render_template("index.html",
                           userName=userName,
                           userAge=userAge,
                           jahAge=jahAge)


@app.route('/shoppinglist', methods=['GET', 'POST'])
def shoppingList():
    url = 'placeholder'
    shopping_list = 'placeholder'
    error = None

    if request.method == 'POST' and ('url' in request.form):
        url = str(request.form.get('url'))
        try:
            shopping_list = str(web_parse.crawl_GPT(url))
        except Exception as e:
            error = str(e)

    return render_template('shoppinglist.html', shopping_list=shopping_list, error=error)


if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
