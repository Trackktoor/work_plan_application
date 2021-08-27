from flask import Flask
import sqlalchemy

from configuration import Configuration

from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from schema.schema import shema

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


