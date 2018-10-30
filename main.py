from flask import Flask, make_response, redirect

app = Flask(__name__)


@app.route('/yay/<smth>')
def index(smth):
    response = make_response('{} with cookie'.format(smth))
    response.set_cookie('my_cookie', '666')
    return response


@app.route('/google')
def google():
    return redirect('http://google.com')


@app.route('/err')
def err():
    return 'error', 400


if __name__ == '__main__':
    app.run(debug=True)
