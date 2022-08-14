#!/home/inyoka/flask/basics/.env_basics/bin/python


from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Index page</h1>'

@app.route('/somepage')
def somepage():
    return '<h1>Somepage page</h1>'

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Page does not exist!!!</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    return f'<h1>This is a page for {name.upper()}.</h1>'


@app.route('/latin/<name>')
def latin(name):
    if name[-1] == 'y':
        name = name[:-1] + 'iful'
    else:
        name = name + 'y'
    return f'<h1>This is a page for {name.upper()}.</h1>'


if __name__ == '__main__':
    app.run(debug=True)
