
import logging.config
import os
from flask import Flask, Blueprint
from flask_restplus import Api
from flask_restplus import Resource

from api.people import api as PeopleSpace
from api.employee import api as EmployeeSpace

from flask import jsonify

from flask.views import MethodView

log = logging.getLogger(__name__)

app = Flask(__name__)

api = Api(app, version='1.0', title='My Planet API',
          description='A Demo for my planet powered API --  Eric ( ericlzyu@gmail.com ) ')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)


class PingPongView(MethodView):
    """PingPongView apis"""

    def get(self, *args, **kwargs):
        return jsonify({'message': 'pong'})

app.add_url_rule('/ping/', view_func=PingPongView.as_view('ping'))

def init_app_with_ns(app):
    api.add_namespace(PeopleSpace)
    api.add_namespace(EmployeeSpace)

def main():
    init_app_with_ns(app)
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()