from flask import jsonify, request

from yacut import app
from yacut.exceptions import InvalidAPIUsageError, URLMapNotFoundError
from yacut.models import URLMap
from yacut.utils import add_urlmap_to_db, get_unique_custom_id
from yacut.validators import (
    is_only_letters_and_digits, validate_custom_id, validate_original_link)


@app.route('/api/id/', methods=['POST'])
def api_get_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsageError('Отсутствует тело запроса')
    original = data.get('url')
    custom_id = data.get('custom_id')
    validate_original_link(original)
    if custom_id:
        validate_custom_id(custom_id)
    else:
        custom_id = get_unique_custom_id()
    urlmap = URLMap(original=original, short=custom_id)
    add_urlmap_to_db(urlmap)
    return jsonify(
        dict(short_link=request.root_url + urlmap.short, url=original)), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def api_redirect_to_original(short_id: str):
    if not is_only_letters_and_digits(short_id):
        raise URLMapNotFoundError('Указанный id не найден', 404)
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if not urlmap:
        raise URLMapNotFoundError('Указанный id не найден', 404)
    return jsonify(dict(url=urlmap.original))
