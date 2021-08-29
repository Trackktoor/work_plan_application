class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:roma.ru12@localhost/GraphQLFlaskProject'
    SECRET_KEY = 'roma.ru12'

    ### FLASK_SECURITY ###

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'