from datetime import datetime
from flask import Flask, make_response, redirect, render_template, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/yay/<smth>')
def yay(smth):
    browser = request.user_agent.browser
    response = make_response(f'{smth} with cookie on {browser}')
    response.set_cookie('my_cookie', '666')
    # render_template()
    return response


@app.route('/google')
def google():
    return redirect('http://google.com')


@app.route('/time')
def time():
    return render_template('index.html',
                           current_time=datetime.utcnow())


@app.errorhandler(404)
def not_found(e):
    print('***', e)
    return render_template('404.html'), 404


if __name__ == '__main__':
    manager.run()
    # args: runserver -d -p 5001
