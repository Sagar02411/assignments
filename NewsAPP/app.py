from flask import Flask, jsonify
from database import engine
from models import Base
from tasks import celery_app, fetch_and_store_news
from dotenv import load_dotenv


# from extensions import db, alembic

# Base.metadata.create_all(bind=engine)

app = Flask(__name__)
# db.init(app)
# alembic.init_app(app)


@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "running",
                    "message": "hello owrld"})

@app.route('/fetch', methods=['GET'])
def fetch_now():
    fetch_and_store_news.delay()
    return jsonify({"status": "queued", 
                    "message": "smth"})

if __name__ == '__main__':
    app.run(debug=True)
    
    
# celery -A tasks.celery_app worker --loglevel=info
# celery -A tasks.celery_app beat --loglevel=info