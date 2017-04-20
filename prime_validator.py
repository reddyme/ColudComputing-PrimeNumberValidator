from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/login')
def index():
    return '<html>\
            <head>\
            <style>\
            body{background-image: url("static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}\
            .center{\
            position:absolute;\
            height: X px;\
            width: Y px;\
            left:40%;\
            top:30%;\
            margin-top:- X/2 px;\
            margin-left:- Y/2 px;\
            }\
            </style>\
            </head>\
            <body>\
            <div class="center">\
            <form action = "http://50.112.32.181:5000/calc" method="POST">\
            <h1>Enter a number to check prime or not:</h1>\
            <p><input type="number" name="nm" style="width: 100px;height:30px" /></p>\
            <p><input type="submit" value="Submit" style="height:50px; width:100px"/></p>\
            </form>\
            </div>\
            </body></html>'

@app.route('/success/<name>')
def success(name):
   print 'Given number is: %s' % name
   if int(name)<0:
      return '<html>\
            <head>\
            <style>\
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}\
            .center{\
            position:absolute;\
            height: X px;\
            width: Y px;\
            left:40%;\
            top:30%;\
            margin-top:- X/2 px;\
            margin-left:- Y/2 px;\
            }\
            </style>\
            </head>\
            <body>\
            <div class="center">\
            <h1>Negative numbers cannot be prime</h1>\
            </div></body></html>'
   a=2
   count=0
   name=int(name)
   while name>a:
      if name%a==0 & a!=name:
         count+=1
         break
      a+=1
   if count==0:
      return '<html>\
            <head>\
            <style>\
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}\
            .center{\
            position:absolute;\
            height: X px;\
            width: Y px;\
            left:40%;\
            top:30%;\
            margin-top:- X/2 px;\
            margin-left:- Y/2 px;\
            }\
            </style>\
            </head>\
            <body>\
            <div class="center">\
            <h1>Given number is prime</h1>\
            </div></body></html>'
   else:
      return '<html>\
            <head>\
            <style>\
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}\
            .center{\
            position:absolute;\
            height: X px;\
            width: Y px;\
            left:40%;\
            top:30%;\
            margin-top:- X/2 px;\
            margin-left:- Y/2 px;\
            }\
            </style>\
            </head>\
            <body>\
            <div class="center">\
            <h1>Given number is not prime</h1>\
            </div></body></html>'

@app.route('/calc',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      num = request.form['nm']
      return redirect(url_for('success',name = num))
   else:
      num = request.args.get('nm')
      return redirect(url_for('success',name = num))

