from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def start():
    # return "Hi Welcome"
    # print('Hello World')
    # return '''<html>
    # <head>
    # <title> Home Page </title>
    # </head>

    # <body>
    # <h1> Hello World</h1>
    # </body>
    # </htlm>'''
    
    print(render_template('start.html'))
    return render_template('start.html')

    
@app.route('/home')
def home():
    print(request.args)
    name = request.args.get('name')
    if name == None:
        name = 'Guest'
    return render_template('home.html',name = name,r = 10,arr  = [10,33,21,44,52])
    # return "Hello Welcome to Home"


@app.route('/form',methods = ['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        print(request.form)
        digit_file = request.files.get('digit')
        print(digit_file)
        digit_file.save('./file.png')
        return f"<html><head></head><body><h1>Thank you {request.form.get('fname')} {request.form.get('lname')} </h1></body></html>"


if __name__ == '__main__':
    app.run(use_reloader = True,debug = True)





    