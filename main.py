from flask import Flask, make_response, redirect, render_template
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/yay/<smth>')
def index(smth):
    response = make_response(f'{smth} with cookie')
    response.set_cookie('my_cookie', '666')
    return response


@app.route('/google')
def google():
    return redirect('http://google.com')


@app.route('/err')
def err():
    return 'error', 400


@app.errorhandler(404)
def not_found(a):
    print(a)
    return render_template('404.html'), 404


if __name__ == '__main__':
    manager.run()
    # args: runserver -d -p 5001
