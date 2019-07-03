from flask import Flask, redirect, url_for, render_template,request,Response

response=Response()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

@app.after_request
def add_header(response):
        response.headers['Cache-Control']='no-cache,no-store,must-revalidate'
        response.headers['Expires'] = 0
        response.headers['Pragma'] = 'no-cache'
        return response

@app.route('/index2',methods= ['POST','GET'])
def index2():

        import templates.webcampicturecapture as web
        web.capture()

        import templates.main as mai
        mai.hello()

        return render_template('index2.html')
   
if __name__ == "__main__":
    app.run(host='0.0.0.0')

