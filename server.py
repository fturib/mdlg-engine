from bottle import Bottle, run, template, request
from demo import run_demo

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/demo/<foldername>')
def demofolder(foldername):
    run_demo(foldername)
    return template("<p>Demo ran for the folder <b>{{folderdir}}</b></p>", folderdir=foldername)
    # in case of exception, the stacktrace will be visible in the returned value

@app.route('/demo')
def demo():
    foldername = request.query.dir or "/data/demo"
    run_demo(foldername)
    return template("<p>Demo ran for the dir <b>{{folderdir}}</b></p>", folderdir=foldername)
    # in case of exception, the stacktrace will be visible in the returned value


#run(app, host='localhost', port=8080)