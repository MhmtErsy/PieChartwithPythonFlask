from flask import Flask, render_template, json

app = Flask(__name__)


@app.route('/')
def anasayfa():
    data = {'devices':
                {'Asus': 5648,
                 'Mac': 31234,
                 'HP': 2006,
                 }
            }
    topv = 0
    for key,value in data['devices'].items():
        topv += value

    return render_template("home.html",data=data,topv=topv)


if __name__ == '__main__':
    app.run(debug=True)
