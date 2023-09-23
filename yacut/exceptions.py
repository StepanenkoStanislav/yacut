from http import HTTPStatus


class InvalidAPIUsageError(Exception):
    """Ошибка неправильного использования API."""
    def __init__(self, message, status_code=HTTPStatus.BAD_REQUEST):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


class ValidationError(InvalidAPIUsageError):
    """Ошибка при валидации данных."""


class URLMapNotFoundError(InvalidAPIUsageError):
    """Ошибка отсутствия объекта URLMap в БД."""
