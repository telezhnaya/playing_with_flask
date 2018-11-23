# playing_with_flask
My attempt to learn more about Flask, PostgreSQL, Marshmallow, SQLAlchemy and many other cool things


# run
export PYTHONPATH=.
export FLASK_APP=example.app:create_app()
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run


Выставляем PYTHONPATH, чтоб тесты могли импортить модуль
Выставляем FLASK_APP, чтоб bin/flask мог найти приложение
Выставляем FLASK_ENV, в зависимости от того что нам надо, читаем https://12factor.net/ru/ 3 глава про конфиги
Выставляем FLASK_DEBUG, чтоб `flask run` был под дебагом и выводил нам ошики в браузер
Ну и запускаем наше приложение.

В продакшене надо запускать через gunicorn типа так:
`gunicorn -w 2 --max-requests 50 --access-logfile - --error-logfile - -b 0.0.0.0:5017 example.app:create_app()`
