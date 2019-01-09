
#!python 3.6

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def jahTime():
    userName = ''
    userAge = ''
    jahAge = ''
    if request.method == 'POST' and 'userAge' in request.form:
        userName = request.form.get('userName')
        userAge = request.form.get('userAge')
        jahAge = str(round(((float(int(userAge) / 0.69444444444444)) / 60) - 0.5)) + str(' hours and ') + str(round(float(int(userAge) / .69444444444444) % 60)) + str(' minutes') # the - 0.5 is to force rounding down
        #jahAgeDays =
        #jahAgeHrs =
    return render_template("index.html",
                           userName=userName,
                           userAge=userAge,
                           jahAge=jahAge)



if __name__ == '__main__':
    app.run()
