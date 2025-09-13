from flask import Flask,render_template,request
from utility import predictDigit

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('form.html',prediction = None)
    else:
        path = './digit.png'
        request.files.get('digit').save(path)
        return render_template('form.html',prediction = predictDigit(path))


if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)



""" Deployment Options:
- heroku
- vercel
- aws
- azure
- onrender
- github
"""


