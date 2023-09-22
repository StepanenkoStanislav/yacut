import os
from re import compile


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


ORIGINAL_MAX_LENGTH = 256
CUSTOM_ID_MAX_LENGTH = 16
RANDOM_SEQUENCE_LENGTH = 6
ONLY_LETTERS_AND_DIGITS_PATTERN = compile(r'^[a-zA-Z0-9]*$')
URL_PATTERN = compile(
    r'^[a-z]+://'
    r'(?P<host>[^\/\?:]+)'
    r'(?P<port>:[0-9]+)?'
    r'(?P<path>\/.*?)?'
    r'(?P<query>\?.*)?$'
)
