from flask import Blueprint, render_template
from .models import News
 
main = Blueprint('main', __name__)
@main.route("/")
def index():
    news_list = News.query.all()
    return render_template("index.html", news_list=news_list)