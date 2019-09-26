worker: rake jobs:work
web: gunicorn gettingstarted.wsgi --log-file -
