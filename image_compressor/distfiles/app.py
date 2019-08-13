from flask import *
import os
import random
import re

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['SECRET_KEY'] = os.urandom(32)

HOST, PORT = '0.0.0.0', '13001'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('Upload a file.')
        return redirect('/')
    
    f = request.files['file']
    if not f:
        flash('Upload a file.')
        return redirect('/')
    
    if not is_allowed_file(f.filename):
        flash('Invalid filename.')
        return redirect('/')

    filepath = os.path.join('/tmp', f.filename)
    outpath = '/tmp/{:016x}.zip'.format(random.randrange(0, pow(2, 64)))
    f.save(filepath)
    
    conv = request.form.get('conv', '')
    comp = request.form.get('comp', '')
    enc  = request.form.get('enc' , '')
    password = request.form.get('password', '')
    options = ''
    for option in [conv, comp, enc]:
        if is_allowed_option(option):
            options += '-{} '.format(option)
    if enc and is_allowed_password(password):
        options = '{}"{}"'.format(options, password)
    
    command = 'timeout -k 2 1 zip {} {} -j {}'.format(
        outpath,
        filepath,
        options
    )
    os.system(command)
    
    if not os.path.exists(outpath):
        flash('Failed.')
        return redirect('/')

    response = make_response()
    response.data = open(outpath, "rb").read()
    response.headers['Content-Disposition'] = 'attachment; filename=output.zip'
    response.mimetype = 'application/zip'
    os.unlink(outpath)
    
    return response

def is_allowed_file(filename):
    return re.fullmatch("[A-Za-z0-9]+\.(png|jpg|jpeg)", filename) is not None

def is_allowed_option(option):
    return re.fullmatch("[A-Za-z0-9]+", option) is not None

def is_allowed_password(password):
    return re.fullmatch("[^\"`$\\\\!]+", password) is not None

if __name__ == '__main__':
    app.run(
        host = HOST,
        port = PORT,
        debug=False
    )
