from flask import Flask
import sqlalchemy
from models import db

from configuration import Configuration

from flask_graphql import GraphQLView


from flask_migrate import Migrate

from schema.schema import shema

app = Flask(__name__)
app.config.from_object(Configuration)

db.init_app(app)
migrate = Migrate(app, db)


