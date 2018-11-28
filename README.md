# playing_with_flask
My attempt to learn more about Flask, PostgreSQL, Marshmallow, SQLAlchemy and many other cool things


`flask run -p 5001`

env variables:
`PYTHONUNBUFFERED=1;FLASK_ENV=development;FLASK_DEBUG=1;FLASK_APP=app.app:create_app();PYTHONPATH=.;SECRET_KEY=so secret!;DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/my_db`

Use tags to track the progress.


To create database in Pycharm, press `+` in database menu, fill in details, then in the terminal use
`psql postgres` (if your username is postgres), fill in the password, run `create database my_db;`, return to db menu
and test the connection: it should work. Do not forget to fill in env variables.

To switch on linter:
```
flake8 --install-hook git
git config --bool flake8.strict true
```
