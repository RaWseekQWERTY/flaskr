from flask import(
    Blueprint, views, flash, g, render_template, redirect, session, request,url_for
)
from flaskr.db import get_DB

bp = Blueprint("blog".__name__, url_prefix="/blog")