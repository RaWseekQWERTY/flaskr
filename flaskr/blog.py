from flask import(
    Blueprint, views, flash, g, render_template, redirect, session, request,url_for
)
from flaskr.db import get_DB
from flaskr.auth import login_required

bp = Blueprint("blog".__name__)

@bp.route('/')
def index():
    db = get_DB()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)