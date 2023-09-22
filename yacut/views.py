from flask import abort, redirect, request, render_template, flash, url_for

from yacut import app
from yacut.exceptions import URLMapNotFoundError
from yacut.forms import LinkForm
from yacut.models import URLMap
from yacut.utils import add_urlmap_to_db, get_unique_custom_id
from yacut.validators import is_only_letters_and_digits


@app.route('/', methods=['GET', 'POST'])
def get_short_link():
    form = LinkForm()
    if form.validate_on_submit():
        original_link = form.data.get('original_link')
        custom_id = form.data.get('custom_id')
        if custom_id:
            if URLMap.query.filter_by(short=custom_id).first():
                flash(f'Имя {custom_id} уже занято!')
                return redirect(url_for('get_short_link'))
        else:
            custom_id = get_unique_custom_id()
        urlmap = URLMap(original=original_link, short=custom_id)
        add_urlmap_to_db(urlmap)
        flash('Ваша новая ссылка готова:')
        return render_template(
            'get_short_link.html',
            form=form,
            url=request.root_url + custom_id)
    return render_template('get_short_link.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_to_original(short_id):
    if not is_only_letters_and_digits(short_id):
        raise URLMapNotFoundError('Указанный id не найден', 404)
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if not urlmap:
        flash('Ссылка не найдена')
        abort(404)
    return redirect(urlmap.original), 302
