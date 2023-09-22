from re import fullmatch

from settings import (ONLY_LETTERS_AND_DIGITS_PATTERN,
                      URL_PATTERN,
                      ORIGINAL_MAX_LENGTH,
                      CUSTOM_ID_MAX_LENGTH)
from yacut.exceptions import ValidationError
from yacut.models import URLMap


def validate_original_link(original: str) -> None:
    """Валидация исходной ссылки."""
    if not original:
        raise ValidationError('"url" является обязательным полем!')
    if len(original) > ORIGINAL_MAX_LENGTH:
        raise ValidationError('Длина ссылки "url" должна быть не '
                              f'больше {ORIGINAL_MAX_LENGTH}.')
    if not fullmatch(URL_PATTERN, original):
        raise ValidationError('Некорректная ссылка "url"')


def is_only_letters_and_digits(sequence: str) -> None:
    """Проверка, что последовательность содержит только ascii буквы и цифры."""
    return fullmatch(ONLY_LETTERS_AND_DIGITS_PATTERN, sequence)


def validate_custom_id(custom_id: str) -> None:
    """Валидация короткой ссылки, отправленной пользователем."""
    if len(custom_id) > CUSTOM_ID_MAX_LENGTH:
        raise ValidationError('Указано недопустимое имя для короткой ссылки')
    if not is_only_letters_and_digits(custom_id):
        raise ValidationError('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=custom_id).first():
        raise ValidationError(f'Имя "{custom_id}" уже занято.')
