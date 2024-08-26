from flask import Blueprint, render_template, request, flash
from .models import Message, Log
from sqlalchemy import cast, String

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query_limit = 100

    if request.method == 'POST':
        address = request.form['address']
        if address:
            log_query = Log.query.with_entities(
                cast(Log.id, String).label('id'),
                cast(Log.created, String).label('created'),
                cast(Log.int_id, String).label('int_id'),
                cast(Log.str, String).label('str'),
                cast(Log.address, String).label('address')
            ).filter(Log.address == address)

            message_query = Message.query.with_entities(
                cast(Message.id, String).label('id'),
                cast(Message.created, String).label('created'),
                cast(Message.int_id, String).label('int_id'),
                cast(Message.str, String).label('str'),
                cast(Message.status, String).label('address')
            ).filter(Message.str.like(f'%{address}%'))

            results = (
                log_query.union(message_query)
                .order_by('int_id', 'created')
                .limit(query_limit)
                .all()
            )

            if len(results) >= query_limit:
                flash('Too many results, showing first 100')

    return render_template('index.html', results=results)