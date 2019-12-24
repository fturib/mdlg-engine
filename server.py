from bottle import Bottle, run, template, request, static_file, abort
from demo import run_demo
import os

app = Bottle()
DATA_DIR = "/data"

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/help')
def help():
    return template("help.tpl")

@app.route('/run/<filepath:path>')
def demopath(filepath):
    foldername = os.path.join(DATA_DIR, filepath)
    run_demo(foldername)
    return template("<p>Demo ran for the filepath <b>{{folderdir}}</b></p>", folderdir=filepath)
    # in case of exception, the stacktrace will be visible in the returned value

def listfiles(relative_path):

    if len(relative_path)>0 and relative_path[1] == '/':
        return abort(404, "invalid path provided : it MUST not be absolute path")

    # Joining the base and the requested path
    abs_path = os.path.join(DATA_DIR, relative_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404, "the path provided does not match any existing file or dir")

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        download = 'download' in request.query
        return static_file(relative_path, DATA_DIR, download=download)

    # Show directory contents
    files = []
    dirs = []
    content = os.listdir(abs_path)
    if len(relative_path) > 0:
        # add the parent dir as ".."
        path = os.path.normpath(os.path.join(abs_path, os.pardir))
        reqpath = os.path.normpath(os.path.join('/files', relative_path, os.pardir))
        dirs.append({'name': os.pardir, 'path': path, 'query': reqpath})

    for n in content:
        path = os.path.join(abs_path, n)
        reqpath = os.path.join('/files', relative_path, n)
        if os.path.isdir(path):
            dirs.append({'name': n, 'path': path, 'query': reqpath})
        else:
            files.append({'name': n, 'path': path, 'query': reqpath})
    return template('files.tpl', files=files, dirs=dirs, folder=relative_path)


@app.route('/files')
def listfilesdata():
    return listfiles("")

@app.route('/files/<req_path:path>')
def listfilesinpath(req_path):
    return listfiles(req_path)



#run(app, host='localhost', port=8080)