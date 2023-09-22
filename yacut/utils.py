from random import choice
from string import ascii_letters, digits

from sqlalchemy.exc import InvalidRequestError

from settings import RANDOM_SEQUENCE_LENGTH
from yacut import db
from yacut.models import URLMap


def add_urlmap_to_db(urlmap: URLMap) -> None:
    """Добавление URLMap в БД."""
    db.session.add(urlmap)
    try:
        db.session.commit()
    except InvalidRequestError as error:
        db.session.close()
        raise error


def get_random_sequence(length: int) -> str:
    """Создание случайной последовательности
     из ascii_letters и digits длиной length.
     """
    return ''.join([choice(ascii_letters + digits) for _ in range(length)])


def get_unique_custom_id() -> str:
    """Создание короткой ссылки yacut."""
    custom_id = get_random_sequence(length=RANDOM_SEQUENCE_LENGTH)
    while URLMap.query.filter_by(short=custom_id).first():
        custom_id = get_random_sequence(length=RANDOM_SEQUENCE_LENGTH)
    return custom_id
