from .extensions import db
from datetime import datetime
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.String(80))
    source_name = db.Column(db.String(100))
    author = db.Column(db.String(80))
    title = db.Column(db.String(80), unique=False)
    description = db.Column(db.Text)
    url = db.Column(db.String(80))
    url_to_image = db.Column(db.String(255))
    published_at = db.Column(db.String(80))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)