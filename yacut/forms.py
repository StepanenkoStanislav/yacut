from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, URL, Regexp

from settings import (ONLY_LETTERS_AND_DIGITS_PATTERN,
                      CUSTOM_ID_MAX_LENGTH,
                      ORIGINAL_MAX_LENGTH)


class LinkForm(FlaskForm):
    """Форма для передачи ссылки и возможного варианта короткой ссылки."""

    original_link = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired('Обязательное поле'),
            Length(
                0,
                ORIGINAL_MAX_LENGTH,
                message=f'Ссылка должна быть не длиннее {ORIGINAL_MAX_LENGTH}'
            ),
            URL(message='Некорректная ссылка')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                0,
                CUSTOM_ID_MAX_LENGTH,
                message=('Ваш вариант короткой ссылки должен быть '
                         f'не длиннее {CUSTOM_ID_MAX_LENGTH}')
            ),
            Regexp(
                regex=ONLY_LETTERS_AND_DIGITS_PATTERN,
                message='Ваша короткая ссылка должна содержать '
                        'только буквы и цифры'),
        ]
    )
